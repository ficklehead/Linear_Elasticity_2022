import numpy as np
import matplotlib.pyplot as plt


def plot_trajectory(solid, movement):
    for i in range(len(solid.material_points)):
        plt.plot(movement.point_trajectories[i].x, movement.point_trajectories[i].y, 'g')
        plt.plot(solid.material_points[i].x, solid.material_points[i].y, 'r.')
        n = len(solid.material_points) - 1
        plt.plot(movement.point_trajectories[i].x[n], movement.point_trajectories[i].y[n], 'b.')

    plt.axis('equal')
    plt.grid()
    plt.savefig('plots/plot_trajectory.svg', format='svg', dpi=1200)
