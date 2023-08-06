import math

import torch as th


def ula_step(score_fn, x, sq_dt=0.1, energy_scale=1.0):
    grad = score_fn(x) * energy_scale
    return x - 0.5 * sq_dt ** 2 * grad + sq_dt * th.randn_like(x)


def ula(score_fn, x, n_step, dt=0.1, energy_scale=1.0):
    sq_dt = math.sqrt(dt)
    for _ in range(n_step):
        x = ula_step(score_fn, x, sq_dt, energy_scale)
    return x
