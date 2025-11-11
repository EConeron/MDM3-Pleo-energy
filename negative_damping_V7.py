import numpy as np
import matplotlib.pyplot as plt
import math

dt = 0.01
T =  60 * 20
time = np.arange(0, T, dt)

mass = 2e6

k = ((4 * (math.pi ** 2)) * mass) / 3600

wind = 14

v_old = 0.0
def drag_force(velocity, t):
    # gust = 0
    # range = 5
    # shift = 0
    # if shift + range > t % 60 > shift - range:
    #     gust = 0

    v_rel = wind - velocity
    if v_rel > 25:
        return 0
    if v_rel > 12:
        return 16e6 / v_rel
    if v_rel <= 0:
        return 0
    else :
        return (16 / 27) * 0.5 * 1.225 * (125 ** 2) * math.pi * v_rel **2

def mooring_force(position):
     D = 50 #depth
     Lo = 50
     if position == 0:
         return 0

     return  k * ( Lo - ( position**2 + D**2)**0.5 ) *  ( ( position/(position**2 + D**2)**0.5 ) )

    #return -k * position

def sphere_drag(velocity):
    rho = 1027
    area = 0.5 * 3 * math.pi * (6.77**2)
    cd = 0.2
    return -0.5 * rho * area * cd * velocity * abs(velocity)



position = 0
velocity = 0

positions = []
velocities = []


def marine_thruster(position,velocity):
    marine_force_limit = 5e5
    marine_force_constant = 5e5
    if abs(velocity)*marine_force_constant >marine_force_limit:
        if velocity > 0:
            return -marine_force_limit
        else:
            return marine_force_limit
    else:
        if velocity > 0:
            return -marine_force_constant*abs(velocity)
        else:
            return marine_force_constant*abs(velocity)



for t in time:

    F_drag = drag_force(velocity, t)
    F_mooring = mooring_force(position)
    F_damping = sphere_drag(velocity)
    F_thruster = marine_thruster(position, velocity)

    total_force = F_mooring + F_drag + F_damping  - 1/2 * 1.9 * 1027 * 250 * 1 *velocity * abs(velocity)
    acceleration = total_force / mass

    velocity += acceleration * dt
    position += velocity * dt

    positions.append(position)
    velocities.append(velocity)

# fig,axes = plt.subplots(1,2,figsize=(12,6))
# axes[0].set_title('Wind speed set to 14 m/s',fontsize=12)
# axes[0].plot(time, positions)
# axes[0].set_ylabel('Displacement(m)',fontsize=12)
# axes[0].set_xlabel('Time (s)',fontsize=12)

#plt.savefig('displacement2.png')
plt.plot(time,positions)
plt.xlabel('Time (s)')
plt.ylabel('displacement (m)')
plt.show()

plt.plot(time,velocities)
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.show()











import numpy as np
import matplotlib.pyplot as plt
import math

dt = 0.01
T =  60 * 5
time = np.arange(0, T, dt)

mass = 2e6

k = ((4 * (math.pi ** 2)) * mass) / 3600

wind = 14

v_old = 0.0
def drag_force(velocity, t):
    # gust = 0
    # range = 5
    # shift = 0
    # if shift + range > t % 60 > shift - range:
    #     gust = 0

    v_rel = wind - velocity
    if v_rel > 25:
        return 0
    if v_rel > 12:
        return 16e6 / v_rel
    if v_rel <= 0:
        return 0
    else :
        return (16 / 27) * 0.5 * 1.225 * (125 ** 2) * math.pi * v_rel **2

def mooring_force(position):
     D = 50 #depth
     Lo = 50
     if position == 0:
         return 0

     return  k * ( Lo - ( position**2 + D**2)**0.5 ) *  ( ( position/(position**2 + D**2)**0.5 ) )

    #return -k * position

def sphere_drag(velocity):
    rho = 1027
    area = 0.5 * 3 * math.pi * (6.77**2)
    cd = 0.2
    return -0.5 * rho * area * cd * velocity * abs(velocity)



position = 0
velocity = 0

positions = []
velocities = []


def marine_thruster(position,velocity):
    marine_force_limit = 5e5
    marine_force_constant = 5e5
    if abs(velocity)*marine_force_constant >marine_force_limit:
        if velocity > 0:
            return -marine_force_limit
        else:
            return marine_force_limit
    else:
        if velocity > 0:
            return -marine_force_constant*abs(velocity)
        else:
            return marine_force_constant*abs(velocity)



for t in time:

    F_drag = drag_force(velocity, t)
    F_mooring = mooring_force(position)
    F_damping = sphere_drag(velocity)
    F_thruster = marine_thruster(position, velocity)

    total_force = F_mooring + F_drag + F_damping + F_thruster  #- 1/2 * 1.9 * 1.225 * 250 * 30 *velocity * abs(velocity)
    acceleration = total_force / mass

    velocity += acceleration * dt
    position += velocity * dt

    positions.append(position)
    velocities.append(velocity)


# axes[1].plot(time, positions)
# # plt.title('Displacement against time for complete computational model')
# axes[1].set_title('Wind speed set to 14 m/s with marine thruster' ,fontsize=12)
#
#
# fig.suptitle('Displacement against time for computational model with drag resistance',fontsize=15)
# plt.tight_layout()
# axes[1].set_xlabel('Time (s)',fontsize=12)
# # plt.savefig('thruster_displacement.png')
# plt.show()

# plt.plot(time, velocities)
# plt.xlabel('Time (s)')
# plt.ylabel('Velocity (m/s)')
# plt.show()






