#matplotlib inline

"""
Simulate quadrotor
"""

import numpy as np
from math import sin, cos, pi
from trajectories import *
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import importlib

from quad_sim import simulate_quadrotor

# Need to reload the module to use the latest code
import quadrotor
importlib.reload(quadrotor)
from quadrotor import Quadrotor

# Weights of LQR cost
R = np.eye(2);
Q = np.diag([10, 10, 1, 1, 1, 1]);
Qf = Q;

# End time of the simulation
tf = 2*pi;

# Construct our quadrotor controller 
quadrotor = Quadrotor(Q, R, Qf, tf);

# Set quadrotor's initial state and simulate
x0 = 2.0 * np.ones((6,)) + x_d(0.0)
x, u, t = simulate_quadrotor(x0, tf, quadrotor)

"""
Create animation 
"""
import create_animation
importlib.reload(create_animation)
from create_animation import create_animation

# Number of poses to visualize 
# TODO: set this value to 60 for the final plots
n_frame = 30

anim, fig = create_animation(x, x_d, tf, n_frame)
plt.show()
anim

# Save the trajectory figure to workspace
# Remember to download the figure of either stable/unstable trajectory before overwriting the previous one
fig.savefig("quadrotor_trajectory.png", dpi=240)