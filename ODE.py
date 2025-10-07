import numpy as np 
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

p_air = 1.204
p_water = 1000
v_wind = 6
A2 = 50
A1 = 100
A = A1 + A2
L0 = 1000
C = 1.98
k = 1e6


def F_wind(p, v, A):
    return 1/2 * p * v**2


a = F_wind(p_air, v_wind, A)
b = 1/2 * p_air * C * A1 + 1/2 * p_water * C * A2#
c = k
d = L0
e = 1e6

def system(t, y):

    x, v = y
    sys = [v, (a- b*v**2 - x*(c-d/(np.sqrt(x**2 + d**2))))/e]

    return sys

# Initial conditions
x0, v0 = 0, 0

t_span = (0, 50)
t_eval = np.linspace(*t_span, 2000)

# Solve the system
sol = solve_ivp(system, t_span, [x0, v0], t_eval=t_eval)

# Plot displacement vs time
plt.figure(figsize=(8,4))
plt.plot(sol.t, sol.y[0], label="x(t)")
plt.xlabel("Time (s)")
plt.ylabel("Displacement (m)")
plt.title("Platform Surge Displacement vs Time")
plt.grid(True)
plt.legend()
plt.show()