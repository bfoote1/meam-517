import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
from random import uniform

def unicycle_spline(t0, tf, obs):
    #UNICYCLE_SPLINE returns a spline object representing a path from
    # (y(t0),z(t0)) = (0,0) to (y(t0),z(t0)) = (10,0) that avoids the two
    # circular obstacles in obs, such that d\dt y(t) > 0
    #   @param t0 - initial time
    #   @param tf - final time
    #
    #   @output y_spline - spline object for desired y trajectory
    #   @output z_spline - spline object for desired z trajectory
    y0 = 0;
    z0 = 0;

    yf = 10;
    zf = 0;

    y1_left = obs.obstacle_1_x - (obs.obstacle_1_radius / 2.0)
    y1_center = obs.obstacle_1_x
    y1_right = obs.obstacle_1_x + (obs.obstacle_1_radius / 2.0)
    y2_left = obs.obstacle_2_x - (obs.obstacle_2_radius / 2.0)
    y2_center = obs.obstacle_2_x
    y2_right = obs.obstacle_2_x + (obs.obstacle_2_radius / 2.0)

    z1 = obs.obstacle_1_y - obs.obstacle_1_radius - 1.0
    z2 = obs.obstacle_2_y + obs.obstacle_2_radius + 1.0

    # TODO: design the spline here
    t = np.array([t0, t0 + (y1_left / 10) * (tf - t0), t0 + (y1_center / 10) * (tf - t0), t0 + (y1_right / 10) * (tf - t0),t0 + (y2_left / 10) * (tf - t0), t0 + (y2_center / 10) * (tf - t0), t0 + (y2_right / 10) * (tf - t0), tf])
    y = np.array([y0, y1_left, y1_center, y1_right, y2_left, y2_center, y2_right, yf])
    z = np.array([z0, z1, z1, z1, z2, z2, z2, zf])

    y_spline = CubicSpline(t, y);
    z_spline = CubicSpline(t, z);


    return y_spline, z_spline
