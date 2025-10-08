import numpy as np
import matplotlib.pyplot as plt

dt = 0.01
T = 1000
time = np.arange(0, T, dt)

mass = 5e6
k = 2e4
damping = 0.0

wind = 12.0
drag_constant = 5e3

def drag_force(velocity):
    v_rel = wind - velocity
    if v_rel > 0:
        return drag_constant * v_rel
    else:
        return 0.0

def mooring_force(position):
    return -k * position

position = 1.0
velocity = 0.0

positions = []
velocities = []

for t in time:
    F_drag = drag_force(velocity)
    F_mooring = mooring_force(position)
    F_damping = -damping * velocity

    total_force = F_mooring - F_drag + F_damping
    acceleration = total_force / mass

    velocity += acceleration * dt
    position += velocity * dt

    positions.append(position)
    velocities.append(velocity)

plt.plot(time, positions)
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.show()
