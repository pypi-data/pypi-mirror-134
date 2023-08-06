import torch as t
import torch.nn.functional as F
from torch import nn

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
        self.net = NonlocalNet()
        self._load_ckpt()

    def _load_ckpt(self):
        import os

        import gdown

        ckpt_dir = os.getenv(
            "JAM_DISTPATH", os.path.expanduser("~/dpdata/jamdist/ckpt/")
        )
        if not os.path.exists(ckpt_dir):
            os.makedirs(ckpt_dir, exist_ok=True)
        ckpt_path = os.path.join(ckpt_dir, "flowers_convergent_net.pth")
        if not os.path.exists(ckpt_path):
            gdown.download(id="1BQOhJ1M6rZjUpILiiUYRqx6F7A5BJakc", output=ckpt_path)
        self.net.load_state_dict(t.load(ckpt_path, map_location="cpu"))

    def forward(self, x):
        return self.net(x)

    def log_prob(self, x):
        return self.net(x)

    # def sample(self, batch_size):
    #     x_s_t = t.autograd.Variable(x_s_t_0.clone(), requires_grad=True)

    #     epsilon =  7.5e-3
    #     log_freq = 500
    #     # sampling records
    #     grads = t.zeros(250000, batch_size)
    #     ens = t.zeros(250000, batch_size)

    #     # iterative langevin updates of MCMC samples
    #     for ell in range(250000):
    #         en = self.forward(x_s_t)
    #         ens[ell] = en.detach().cpu()
    #         grad = t.autograd.grad(en.sum(), [x_s_t])[0]
    #         if epsilon > 0:
    #             x_s_t.data += - ((epsilon**2)/2) * grad + epsilon * t.randn_like(x_s_t)
    #             grads[ell] = ((epsilon**2)/2) * grad.view(grad.shape[0], -1).norm(dim=1).cpu()
    #         else:
    #             x_s_t.data += - grad
    #             grads[ell] = grad.view(grad.shape[0], -1).norm(dim=1).cpu()
    #         if ell == 0 or (ell + 1) % log_freq == 0 or (ell + 1) == 250000:
    #             print('Step {} of {}.   Ave. En={:>14.9f}   Ave. Grad={:>14.9f}'.
    #                 format(ell+1, 250000, ens[ell].mean(), grads[ell].mean()))
    #     return x_s_t.detach(), ens, grads
