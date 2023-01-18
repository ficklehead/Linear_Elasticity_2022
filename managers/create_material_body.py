import managers.functions as fun
import numpy as np
from models.material_body import MaterialBody
from models.material_point import MaterialPoint

t = 0


def create_material_point(x0, y0, r, k):
    material_points = []

    alfa = np.linspace(0, np.pi / 2, k)
    x_vector = []
    y_vector = []
    x_vector = x0 + r * np.sin(alfa)
    y_vector = y0 + (r - r * np.cos(alfa))

    print(x_vector)
    print(y_vector)

    for i in range(0, k-1):
        print('vector ', x_vector[i])
        material_points.append(MaterialPoint(i, x_vector[i], y_vector[i], fun.xfunction(t, x_vector[i]), fun.yfunction(t, y_vector[i]), t))
    return material_points


def create_material_body(material_points):
    material_body = MaterialBody(material_points, t)
    return material_body
