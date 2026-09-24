import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

def unicycle_input(t, y_spline, z_spline):
    #UNICYCLE_INPUT returns input to the unicycle
    #   @param t - current time
    #   @param y_spline - spline object for desired y trajectory
    #   @param z_spline - spline object for desired z trajectory
    #   
    #   @output u - input u(t) to the unicycle system

    # TODO: modify u to return the correct input for time t.
    u1 = (z_spline(t, 2) * y_spline(t, 1) - z_spline(t, 1) * y_spline(t, 2)) / ((y_spline(t, 1)**2 + z_spline(t, 1)**2))
    u2 = np.sqrt(y_spline(t, 1)**2 + z_spline(t, 1)**2)

    u = np.array([u1, u2])


    return u
