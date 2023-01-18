import numpy as np
from models.space_point import SpacePoint
from models.space_grid import SpaceGrid
from managers.functions import *


def create_space_point(t, n):
    h = t / n
    x = np.arange(-4, 4, 16)
    y = np.arange(-4, 4, 16)
    for t in range(0, t, h):
        space_points = []
        for i in range(16):
            for j in range(16):
                x_space = x[i, j]
                y_space = y[i, j]
                space_points.append(
                    SpacePoint(i + j, x_space, y_space, xfunction(t, x_space), yfunction(t, y_space), t))
    return space_points


def create_space_grid(t, n, space_points):
    h = t / n
    space_grid = []
    for t in range(0, t, h):
        space_grid.append(SpacePoint(space_points))
    return space_grid
