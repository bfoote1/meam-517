# HW1 Problem 5

import numpy as np
import matplotlib.pyplot as plt

# Part C: Plot 2D phase portrait of the system

stable_equilibrium = [-1, 2]

x1_range = [stable_equilibrium[0] - 4, stable_equilibrium[0] + 4]
x2_range = [stable_equilibrium[1] - 4, stable_equilibrium[1] + 4]
x1 = np.linspace(x1_range[0], x1_range[1], 21)
x2 = np.linspace(x2_range[0], x2_range[1], 21)
X1, X2 = np.meshgrid(x1, x2)

x1_dot = X2 - 2
x2_dot = -X1 - X2 + (1/3)*(X1 + 1)**3 + 1

magnitude = np.sqrt(x1_dot**2 + x2_dot**2)
x1_dir = np.divide(x1_dot, magnitude, out=np.zeros_like(x1_dot), where=magnitude != 0)
x2_dir = np.divide(x2_dot, magnitude, out=np.zeros_like(x2_dot), where=magnitude != 0)

plt.quiver(X1, X2, x1_dir, x2_dir)

#plt.quiver(X1, X2, x1_dot, x2_dot)
plt.plot(-1, 2, 'o')
plt.plot(-1 + np.sqrt(3), 2, 'x')
plt.plot(-1 - np.sqrt(3), 2, 'x')

# Part D: Overlay an approximation for the boundary of the region of attration for
# the stable equilibrium point

from scipy.spatial import ConvexHull
from scipy.integrate import solve_ivp

stable_equilibrium = np.array([-1, 2])
tolerance = 1e-3

def f(t, x):
    x1 = x[0]
    x2 = x[1]

    x1_dot = x2 - 2
    x2_dot = -x1 - x2 + (1/3)*(x1 + 1)**3 + 1

    return [x1_dot, x2_dot]

points = []

for i in range(X1.shape[0]):
    for j in range(X1.shape[1]):
        x0 = [X1[i, j], X2[i, j]]

        sol = solve_ivp(f, [0, 100], x0)

        if np.linalg.norm(sol.y[:, -1] - stable_equilibrium) < tolerance:
            points.append(x0)

points = np.array(points)
hull = ConvexHull(points)

for simplex in hull.simplices:
    plt.plot(points[simplex, 0],points[simplex, 1])

# Part E: Simulate the system for two initial conditions: one inside the region of
# attraction and one outside the region of attraction

x0_inside = [-3, 5]
x0_outside = [-1, 5]
t_span = (0,20)

sol_inside = solve_ivp(f, t_span, x0_inside)
sol_outside = solve_ivp(f, t_span, x0_outside)

plt.plot(sol_inside.y[0, :], sol_inside.y[1, :])
plt.plot(x0_inside[0], x0_inside[1], 'o')

plt.plot(sol_outside.y[0, :], sol_outside.y[1, :])
plt.plot(x0_outside[0], x0_outside[1], 'o')

plt.xlim(x1_range)
plt.ylim(x2_range)

plt.show()
