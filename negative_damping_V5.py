import numpy as np
import matplotlib.pyplot as plt
import math

dt = 0.1
T = 20 * 60
time = np.arange(0, T, dt)

mass = 2e6

k = ((4 * (math.pi ** 2)) * mass) / 3600

wind = 20

v_old = 0.0
def drag_force(velocity, t):
    gust = 0
    range = 5
    shift = 0
    if shift + range > t % 60 > shift - range:
        gust = 0

    v_rel = wind - velocity + gust
    if v_rel > 25:
        return 0
    if v_rel > 12:
        return 16e6 / v_rel
    if v_rel < 0:
        return 0
    else :
        return (16 / 27) * 0.5 * 1.225 * (125 ** 2) * math.pi * v_rel **2

def mooring_force(position):
    D = 1000
    L = 100
    # return  -k * ( (position**2 + D**2)**0.5 -L ) * (position/abs(position)) * math.cos(math.atan(D/position))

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
    return -0.5 * rho_water * cd_combined * effective_area * velocity * abs(velocity)



position = 0
velocity = 1

positions = []
velocities = []

for t in time:
    F_drag = drag_force(velocity, t)
    F_mooring = mooring_force(position)
    F_damping = sphere_drag(velocity)

    total_force = F_mooring + F_drag # F_damping
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



