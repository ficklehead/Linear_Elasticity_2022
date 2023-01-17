from material_point import MaterialPoint
from typing import List


class PointTrajectory:
    def __init__(self, id, x_coords: List[float], y_coords: List[float]):
        self.id = id
        self.x_coords = x_coords
        self.y_coords = y_coords
