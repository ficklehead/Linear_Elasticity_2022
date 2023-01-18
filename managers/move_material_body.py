from managers.integrate_by_runge_kutt import runge_kutt_4
from models.point_trajectory import PointTrajectory
from models.body_trajectory import BodyTrajectory


def move_material_point(t, n, solid):
    points_trajectory = []
    for i in range(len(solid.material_points)):
        x0 = solid.material_points[i].x
        y0 = solid.material_points[i].y

        x = runge_kutt_4(t, x0, n, 1)
        print(x)
        y = runge_kutt_4(t, y0, n, 0)
        print(y)
        points_trajectory.append(PointTrajectory(i, x, y, solid.material_points[i]))

    return points_trajectory


def move_material_body(points_trajectory, solid):
    body_trajectory = BodyTrajectory(points_trajectory, solid)
    return body_trajectory
