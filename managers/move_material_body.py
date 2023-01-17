from models.material_body import MaterialBody
from models.material_point import MaterialPoint


def move_material_body(material_body: MaterialBody):
    for material_point in material_body.material_points:
        move_material_point(material_point)
        pass


def move_material_point(material_point: MaterialPoint):
    a1 = material_point.a1

    pass
