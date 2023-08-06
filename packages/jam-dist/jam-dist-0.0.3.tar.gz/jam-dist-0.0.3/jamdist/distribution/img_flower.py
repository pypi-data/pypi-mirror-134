import torch as t
import torch.nn.functional as F
from torch import nn

try:
    from functorch import grad, make_functional, vmap

    AVAILABLE_FT = True
except:
    AVAILABLE_FT = False

# pylint: disable=invalid-name, too-few-public-methods

# https://github.com/point0bar1/ebm-anatomy/blob/master/nets.py
# implementation with minor changes from https://github.com/AlexHex7/Non-local_pytorch
# Original Version: Copyright (c) 2018 AlexHex7


class NonlocalNet(nn.Module):
    def __init__(self, n_c=3, n_f=32, leak=0.05):
        super().__init__()
        self.convs = nn.Sequential(
            nn.Conv2d(
                in_channels=n_c, out_channels=n_f, kernel_size=3, stride=1, padding=1
            ),
            nn.LeakyReLU(negative_slope=leak),
            nn.MaxPool2d(2),
            NonLocalBlock(in_channels=n_f),
            nn.Conv2d(
                in_channels=n_f,
                out_channels=n_f * 2,
                kernel_size=3,
                stride=1,
                padding=1,
            ),
            nn.LeakyReLU(negative_slope=leak),
            nn.MaxPool2d(2),
            NonLocalBlock(in_channels=n_f * 2),
            nn.Conv2d(
                in_channels=n_f * 2,
                out_channels=n_f * 4,
                kernel_size=3,
                stride=1,
                padding=1,
            ),
            nn.LeakyReLU(negative_slope=leak),
            nn.MaxPool2d(2),
        )

        self.fc = nn.Sequential(
            nn.Linear(in_features=(n_f * 4) * 4 * 4, out_features=n_f * 8),
            nn.LeakyReLU(negative_slope=leak),
            nn.Linear(in_features=n_f * 8, out_features=1),
        )

    def forward(self, x):
        conv_out = self.convs(x).view(x.shape[0], -1)
        return self.fc(conv_out).squeeze()


# structure of non-local block (from Non-Local Neural Networks https://arxiv.org/abs/1711.07971)
class NonLocalBlock(nn.Module):
    def __init__(self, in_channels, sub_sample=True):
        super().__init__()

        self.in_channels = in_channels
        self.inter_channels = max(1, in_channels // 2)

        self.g = nn.Conv2d(
            in_channels=self.in_channels,
            out_channels=self.inter_channels,
            kernel_size=1,
            stride=1,
            padding=0,
        )

        self.W = nn.Conv2d(
            in_channels=self.inter_channels,
            out_channels=self.in_channels,
            kernel_size=1,
            stride=1,
            padding=0,
        )
        nn.init.constant_(self.W.weight, 0)
        nn.init.constant_(self.W.bias, 0)
        self.theta = nn.Conv2d(
            in_channels=self.in_channels,
            out_channels=self.inter_channels,
            kernel_size=1,
            stride=1,
            padding=0,
        )
        self.phi = nn.Conv2d(
            in_channels=self.in_channels,
            out_channels=self.inter_channels,
            kernel_size=1,
            stride=1,
            padding=0,
        )

        if sub_sample:
            self.g = nn.Sequential(self.g, nn.MaxPool2d(kernel_size=(2, 2)))
            self.phi = nn.Sequential(self.phi, nn.MaxPool2d(kernel_size=(2, 2)))

    def forward(self, x):

        batch_size = x.size(0)

        g_x = self.g(x).view(batch_size, self.inter_channels, -1)
        g_x = g_x.permute(0, 2, 1)

        theta_x = self.theta(x).view(batch_size, self.inter_channels, -1)
        theta_x = theta_x.permute(0, 2, 1)
        phi_x = self.phi(x).view(batch_size, self.inter_channels, -1)
        f = t.matmul(theta_x, phi_x)
        f_div_c = F.softmax(f, dim=-1)

        y = t.matmul(f_div_c, g_x)
        y = y.permute(0, 2, 1).contiguous()
        y = y.view(batch_size, self.inter_channels, *x.size()[2:])
        w_y = self.W(y)
        z = w_y + x

        return z


class FlowersDist(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = None
        self.data_ndim = 3072
        self.data_shape = (3, 32, 32)
        train_epsilon = 7.5e-3
        self.inv_temp = 2.0 / train_epsilon ** 2

    def _load_ckpt(self):
        import os

        import gdown

        net = NonlocalNet()
        ckpt_dir = os.getenv(
            "JAM_DISTPATH", os.path.expanduser("~/dpdata/jamdist/ckpt/")
        )
        if not os.path.exists(ckpt_dir):
            os.makedirs(ckpt_dir, exist_ok=True)
        ckpt_path = os.path.join(ckpt_dir, "flowers_convergent_net.pth")
        if not os.path.exists(ckpt_path):
            gdown.download(id="1BQOhJ1M6rZjUpILiiUYRqx6F7A5BJakc", output=ckpt_path)
        net.load_state_dict(t.load(ckpt_path, map_location="cpu"))
        net.eval()
        self.net = net.requires_grad_(False)
        self.setup_ft()

    def setup_ft(self):
        if AVAILABLE_FT:
            fmodel, params = make_functional(self.net)

            def get_log_prob(sample):
                batch = sample.unsqueeze(0)
                return fmodel(params, batch)

            ft_compute_grad = grad(get_log_prob)
            self.ft_compute_sample_grad = vmap(ft_compute_grad, in_dims=(0,))

    def to(self, *args, **kwargs):
        super().to(*args, **kwargs)
        self.setup_ft()

    def cuda(self, *args, **kwargs):
        super().cuda(*args, **kwargs)
        self.setup_ft()

    def cpu(self, *args, **kwargs):
        super().cpu(*args, **kwargs)
        self.setup_ft()

    def forward(self, x):
        return self.net(x) * self.inv_temp

    def log_prob(self, x):
        return self.forward(x)

    def score(self, x):
        with t.no_grad():
            if AVAILABLE_FT:
                return self.ft_compute_sample_grad(x)
            else:
                return self.naive_score(x)

    def naive_score(self, x):
        with t.no_grad():
            copy_x = x.detach().clone()
            copy_x.requires_grad = True
            with t.enable_grad():
                self.forward(copy_x).sum().backward()
                return copy_x.grad.data


class MNISTDist(FlowersDist):
    def __init__(self):
        super().__init__()
        self.data_ndim = 1024
        self.data_shape = (1, 32, 32)
        train_epsilon = 7.5e-3
        self.inv_temp = 2.0 / train_epsilon ** 2

    def _load_ckpt(self):
        import os

        import gdown

        net = NonlocalNet(n_c=1)
        ckpt_dir = os.getenv(
            "JAM_DISTPATH", os.path.expanduser("~/dpdata/jamdist/ckpt/")
        )
        if not os.path.exists(ckpt_dir):
            os.makedirs(ckpt_dir, exist_ok=True)
        ckpt_path = os.path.join(ckpt_dir, "mnist_convergent_net.pth")
        if not os.path.exists(ckpt_path):
            gdown.download(id="1f-Irbs_QM7UR6GjeH7actta4VWx2r0Qp", output=ckpt_path)
        net.load_state_dict(t.load(ckpt_path, map_location="cpu"))
        net.eval()
        self.net = net.requires_grad_(False)
        self.setup_ft()
