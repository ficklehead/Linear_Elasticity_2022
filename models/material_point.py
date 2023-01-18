from typing import List
class MaterialPoint:
    def __init__(self, id, x: List[float], y: List[float], vx, vy, time):
        self.id = id
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.time = time
