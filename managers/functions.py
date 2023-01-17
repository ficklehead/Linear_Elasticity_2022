import numpy as np


def xfunction(x, t):
    return np.exp(-t) * x


def yfunction(y, t):
    return (t - 1) * y
