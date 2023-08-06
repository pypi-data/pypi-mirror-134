import numpy as np
import torch as t


def v2_d(vec):
    return t.square(vec).mean()  # v^2 / d shorthand


def l2_norm_flat(vec):
    """Shorthand for squared L2 norm per batch dimension, flattening all dimensions."""
    return t.einsum("j,j", vec.flatten(start_dim=0), vec.flatten(start_dim=0))


# HMC functions
def leapfrog_step(x_0, v_0, score_fn, dt, k, mh_reject=False, log_prob_fn=None):
    """
    A single leapfrog step with energy, f, and optional energy scaling and bounding box (at +/1)
    """
    x_k, v_k = x_0.clone(), v_0.clone()  # used for mh_reject
    for _ in range(k):  # Inefficient version - should combine half steps
        first_grad = score_fn(x_k)
        v_k -= 0.5 * dt * first_grad  # half step in v
        x_k += dt * v_k  # Step in x
        second_grad = score_fn(x_k)
        v_k -= 0.5 * dt * second_grad  # half step in v
    if mh_reject:
        with t.no_grad():
            delta_v = 0.5 * (l2_norm_flat(v_0) - l2_norm_flat(v_k))
            delta_joint_E = log_prob_fn(x_0) - log_prob_fn(x_k) + delta_v
            reject = np.random.random() > t.exp(delta_joint_E).item()
            if reject:
                return x_0, v_0
    return x_k, v_k


def hmc_integrate(
    score_fn, x0, n_step, dt=0.01, k=1, mh_reject=False, log_prob_fn=None
):
    shape = x0.shape
    grad_steps = n_step // k
    xs = t.zeros((grad_steps + 1,) + shape, dtype=x0.dtype)
    vs = t.zeros((grad_steps + 1,) + shape, dtype=x0.dtype)
    xs[0] = x0
    vs[0] = t.randn_like(x0)
    x = x0
    for l in range(1, grad_steps + 1):
        x, v = leapfrog_step(
            x,
            t.randn_like(x),
            score_fn,
            dt,
            k,
            mh_reject=mh_reject,
            log_prob_fn=log_prob_fn,
        )
        xs[l], vs[l] = x, v
    return xs, vs, t.arange(len(xs))
