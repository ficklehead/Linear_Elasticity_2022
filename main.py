from managers.create_material_body import create_material_body
from managers.create_material_body import create_material_point
from managers.move_material_body import move_material_body
from managers.move_material_body import move_material_point
from managers.plot_trajectory import plot_trajectory
from managers.move_through_space import create_space_point
from managers.move_through_space import create_space_grid

x0 = 2
y0 = -6
n = 10
r = 4
t = 1

material_points = create_material_point(x0, y0, r, n)
solid = create_material_body(material_points)

points_trajectory = move_material_point(t, n, solid)
movement = move_material_body(points_trajectory, solid)

space_points = create_space_point(t, n)
grid = create_space_grid(t, n, space_points)

plot_trajectory(solid, movement)
