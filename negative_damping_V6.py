import numpy as np
import matplotlib.pyplot as plt
import math

dt = 0.01
T = 20 * 60
time = np.arange(0, T, dt)

mass = 2e6

k = ((4 * (math.pi ** 2)) * mass) / 3600

wind = 14

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
    if v_rel <= 0:
        return 0
    else :
        return (16 / 27) * 0.5 * 1.225 * (125 ** 2) * math.pi * v_rel **2

def mooring_force(position):
    D = 1000
    L = 100
    # return  -k * ( (position**2 + D**2)**0.5 -L ) * (position/abs(position)) * math.cos(math.atan(D/position))

    return -k * position

def sphere_drag(velocity):
    rho = 1027
    area = 0.5 * 3 * math.pi * (6.77**2)
    cd = 0.2
    return -0.5 * rho * area * cd * velocity * abs(velocity)



position = 0
velocity = 0

positions = []
velocities = []

for t in time:
    marine_force = 500000
    if velocity > 0:
        marine_thruster = -marine_force
    else:
        marine_thruster = marine_force


    F_drag = drag_force(velocity, t)
    F_mooring = mooring_force(position)
    F_damping = sphere_drag(velocity)

    total_force = F_mooring + F_drag  + marine_thruster + F_damping #- 1/2 * 1.9 * 1.225 * 250 * 30 *velocity * abs(velocity)
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



