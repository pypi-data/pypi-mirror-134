"""
Leapfrog Sampler for Energy Sampling Hamiltonian Dynamics with Time Re-scaling
"""
import torch as t

# pylint: disable=line-too-long


def esh_leap_step(
    xs,
    u,
    rs,
    score_fn,
    epsilon,
    grad=None,
    energy_scale=1.0,
    debug=False,
    constraint=False,
):
    """Perform one proper leapfrog step for time-scaled ESH dynamics.
    xs - initial position, (batch_size,...)
    u - unit vector velocity (must be normalized!)
    rs - keeps track of dynamics for velocity magnitude, but value does not affect x, u. Can set to t.zeros(batch_size)
    energy - a pytorch function or module that outputs a scalar (per batch item) of input xs
    grad - You can send in the last grad to avoid recomputing
    energy_scale - scale the energy function by this value (i.e., a temperature)
    debug - Look for NaNs and infinities
    constraint - Bound xs in [-1,1], see "billiards" method.
    """
    xs = t.autograd.Variable(xs, requires_grad=True)
    if grad is None:
        grad = energy_scale * score_fn(xs)

    u, rs, log_delta_t_0 = u_r_step(u, rs, grad, epsilon / 2.0)  # Half step u and r
    xs.data = xs.data + epsilon * u  # Full step x
    if constraint:
        xs.data, u = billiards(xs.data, u)
    grad = energy_scale * score_fn(xs)
    u, rs, log_delta_t_1 = u_r_step(u, rs, grad, epsilon / 2.0)  # half step u and r

    log_delta_t = t.logaddexp(log_delta_t_0, log_delta_t_1)
    if debug and (
        not t.isfinite(rs).all() or not t.isfinite(xs).all() or not t.isfinite(u).all()
    ):  # Slow, debugging
        print(
            "Nan or infinite in rs, xs, u",
            t.isfinite(rs).all(),
            t.isfinite(xs).all(),
            t.isfinite(u).all(),
        )
        print("Energy of xs", score_fn(xs))
        print("Energy of random", score_fn(t.randn_like(xs)))
        import IPython

        IPython.embed()

    return (
        xs,
        u,
        rs,
        grad,
        log_delta_t,
    )  # return x, u, r, and grad to prevent repeat computation in next step


def u_r_step(u, rs, grad, epsilon):
    """Implements the step for the u, r update (time-scaled transformed ESH ODE variables).
    Note that it is re-arranged compared to paper: I was attempting to ensure that exp would underflow rather
    than overflow, and the special case u.e = -1 is treated.
    """
    d = u.shape[1:].numel()
    n_dims = len(u.shape) - 1
    left = (-1,) + (1,) * n_dims  # Used to multiply scalars per batch to tensors

    g_norm = grad.flatten(start_dim=1).norm(dim=1).view(left)  # gradient norm
    grad_e = grad / g_norm  # unit vector in grad direction
    u_dot_e = t.einsum(
        "ij,ij->i", u.flatten(start_dim=1), -grad_e.flatten(start_dim=1)
    ).view(
        left
    )  # u.e

    A2 = (u_dot_e - 1.0) * t.exp(-2 * epsilon * g_norm / d)
    A = 1.0 + u_dot_e + A2
    Z = 1.0 + u_dot_e - A2
    B = 2.0 * t.exp(-epsilon * g_norm / d)
    perp_grad = u + grad_e * u_dot_e
    u = t.where(u_dot_e > -1.0, A * -grad_e + B * perp_grad, grad_e)
    delta_r = t.where(
        u_dot_e.flatten() > -1.0,
        (epsilon * g_norm).flatten() / d + t.log(0.5 * Z.flatten()),
        -(epsilon * g_norm).flatten() / d,
    )  # avoid -inf when u_dot_e = -1
    # u /= Z  # This is probably less computation, but not as numerically stable as ensuring unit vector norm
    u /= u.flatten(start_dim=1).norm(dim=1).view(left)
    # log_delta_t_old = rs + (t.log(t.sinh(epsilon * g_norm / d) + u_dot_e * t.cosh(epsilon * g_norm / d) - u_dot_e) - t.log(g_norm)).squeeze()
    log_delta_t = (
        rs
        + (epsilon * g_norm / d - t.log(2 * g_norm) + t.log(A - u_dot_e * B)).squeeze()
    )
    rs = rs + delta_r
    # print(log_delta_t_old, log_delta_t)
    # print((rs-t.log(t.tensor(d)) + t.log(t.tensor(epsilon))), log_delta_t)
    # import IPython; IPython.embed()
    return u, rs, log_delta_t


def billiards(x, v):
    """Implement HMC step with boundary constraints at +-1, Radford Neal HMC 2012.
    In other words, we imagine an infinite potential at +-1 for each coordinate, and reflect
    trajectories off of it, like billiards.
    """
    while x.abs().max() > 1:
        v = t.where(x.abs() > 1, -v, v)  # reflection of velocity
        x = t.where(x.abs() > 1, x.sign() * 2 - x, x)  # Upper/lower +1/-1
    return x, v


def esh_leap_integrate_chain(
    score_fn,
    x,
    n_steps,
    epsilon,
    store=True,
    reservoir=False,
    v=None,
    energy_scale=1.0,
    constraint=False,
):
    """Integrate starting at x0, using "steps" grad evals. Return the entire chain (store=True) or last step only.
    "Reservoir" sampling keeps a reservoir that ergodically samples from the entire chain.
    bc imposes boundary conditions at +-1"""

    if v is None:
        v = t.randn_like(x)  # u = v / |v|
    v_norm = v.flatten(start_dim=1).norm(dim=1).view((-1,) + (1,) * (len(x.shape) - 1))
    v /= v_norm
    r = t.zeros(len(x), device=x.device, dtype=x.dtype)  # r = log |v|

    if store:  # Store states for visualization
        xs = t.zeros(n_steps + 1, *x.shape, dtype=x.dtype, device="cpu")
        vs = t.zeros(n_steps + 1, *x.shape, dtype=x.dtype, device="cpu")
        rs = t.zeros(n_steps + 1, len(x), dtype=x.dtype, device="cpu")
        xs[0], vs[0], rs[0] = x.cpu(), v.cpu(), r.cpu()
    if reservoir:
        x_res = x.clone()
        u_res = v.clone()
        log_cum_w = t.log(t.zeros_like(r))  # Neg. inf, handled correctly by logaddexp
        if store:
            x_res_hist = t.zeros(n_steps + 1, *x.shape, dtype=x.dtype, device="cpu")
            x_res_hist[0] = x.cpu()

    grad = None
    # print('weight, cum weight, w/cum, Rand, select?')
    for tt in range(n_steps):
        x, v, r, grad, log_delta_t = esh_leap_step(
            x,
            v,
            r,
            score_fn,
            epsilon,
            grad,
            energy_scale=energy_scale,
            constraint=constraint,
        )

        if store:
            xs[tt + 1], vs[tt + 1], rs[tt + 1] = x.cpu(), v.cpu(), r.cpu()
        if reservoir:
            # log_cum_w -= 0.1  # 0.9 moving average  # 0.69  # 0.5 exponential moving average
            log_cum_w = t.logaddexp(log_delta_t, log_cum_w)
            rv = t.rand_like(log_delta_t)
            select_new_sample = t.log(rv) < (log_delta_t - log_cum_w)
            # print(t.exp(log_delta_t), t.exp(log_cum_w), t.exp(log_delta_t) / t.exp(log_cum_w), rv, select_new_sample)
            x_res = t.where(select_new_sample, x.T, x_res.T).T
            u_res = t.where(select_new_sample, v.T, u_res.T).T
            if store:
                x_res_hist[tt + 1] = x_res.cpu()
            # import IPython; IPython.embed()
            # print(select_new_sample)
            # print(tt, select_new_sample.float().mean())

    if store and reservoir:
        return xs, vs, rs, x_res, u_res, x_res_hist
    elif store:
        return xs, vs, rs
    elif reservoir:
        return x, v, r, x_res, u_res
    else:
        return x, v, r


def reservoir_binary_search(
    energy, x, n_steps, epsilon, n_binary, energy_scale=1.0, v=None
):
    """Do regular reservoir sampling, then binary search to refine the sample."""
    x, v, _, x_res, u_res = leap_integrate_chain(
        energy,
        x,
        n_steps,
        epsilon,
        store=False,
        reservoir=True,
        v=v,
        energy_scale=energy_scale,
    )
    for _ in range(n_binary):
        epsilon = 0.5 * epsilon
        x, v, _, x_res, u_res = leap_integrate_chain(
            energy,
            x_res,
            2,
            epsilon,
            store=False,
            reservoir=True,
            v=-u_res,
            energy_scale=energy_scale,
        )
    return x_res
