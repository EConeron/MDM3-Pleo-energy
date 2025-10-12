import numpy as np
import matplotlib.pyplot as plt
import math

dt = 0.01
T = 60 * 20
time = np.arange(0, T, dt)

mass = 2e6

k = ((4*(math.pi**2)) * mass) / 3600

wind = 1.0
drag_constant = 5000

def drag_force(velocity):
    v_rel = wind - velocity
    if v_rel > 12:
        return 2e6
    else:
        return 1.38888e4 * v_rel**2

def mooring_force(position):
    return -k * position

def sphere_drag(velocity):
    rho_water = 1025
    g = 9.81
    radius = 6.77
    diameter = radius * 2
    cross_sectional_area = math.pi * radius ** 2
    effective_area = cross_sectional_area / 2
    froude_number = velocity / math.sqrt(g * diameter)
    cd_base = 0.47 / 2

    if 0.6 < froude_number < 1.2:
        wave_drag_factor = 3.0
        cd_combined = cd_base * wave_drag_factor
    else:
        cd_combined = cd_base
    drag_force = 0.5 * rho_water * cd_combined * effective_area
    return drag_force


position = 1.0
velocity = 0.0

positions = []
velocities = []

for t in time:
    F_drag = drag_force(velocity)
    F_mooring = mooring_force(position)
    F_damping = sphere_drag(abs(velocity)) * velocity * abs(velocity)

    total_force = F_mooring - F_drag - F_damping
    acceleration = total_force / mass

    velocity += acceleration * dt
    position += velocity * dt

    positions.append(position)
    velocities.append(velocity)

plt.plot(time, positions)
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.show()

plt.plot(time, velocities)
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.show()



