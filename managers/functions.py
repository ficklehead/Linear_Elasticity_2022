import numpy as np


def xfunction(t, x: float):
    return np.exp(-t) * x


def yfunction(t, y: float):
    return (t - 1) * y
