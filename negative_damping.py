import numpy as np
import matplotlib.pyplot as plt

I = 8000.0
k = 1
c = 0
V = 12.0

beta0 = 5.0
beta_min = 0.0
theta_th = 2
pitch_time_constant = 1.0
delay = 1

t_end = 600
dt = 0.01
steps = int(t_end / dt)

def torque_coefficient(beta):
    return max(0.1, 1.0 - 0.15 * (beta - beta_min))

time = np.linspace(0, t_end, steps)
theta = np.zeros(steps)
omega = np.zeros(steps)
beta = np.zeros(steps)
aero_torque = np.zeros(steps)

theta[0] = 0.0
omega[0] = 0.0
beta[0] = beta0

delay_steps = int(delay / dt)
theta_buffer = [theta[0]] * delay_steps

for i in range(steps - 1):
    theta_delayed = theta_buffer[0]

    if theta_delayed > theta_th:
        beta_target = beta_min
    else:
        beta_target = beta0

    d_beta = (beta_target - beta[i]) * dt / pitch_time_constant
    beta[i+1] = beta[i] + d_beta

    Ct = torque_coefficient(beta[i])
    Ta = Ct * V**2 * np.cos(theta[i])
    aero_torque[i] = Ta

    torque_net = -k * theta[i] - c * omega[i] + Ta

    alpha = torque_net / I

    omega[i+1] = omega[i] + alpha * dt
    theta[i+1] = theta[i] + omega[i+1] * dt

    theta_buffer.append(theta[i+1])
    theta_buffer.pop(0)

aero_torque[-1] = torque_coefficient(beta[-1]) * V**2 * np.cos(theta[-1])

plt.plot(time, theta)
plt.ylabel('Tip angle θ (rad)')
plt.xlabel('Time (s)')
plt.grid()
plt.show()

plt.plot(time, beta,)
plt.ylabel('Pitch angle β (deg)')
plt.xlabel('Time (s)')
plt.grid()
plt.show()

plt.plot(time, aero_torque)
plt.ylabel('Aerodynamic Torque Ta (Nm)')
plt.xlabel('Time (s)')
plt.grid()
plt.show()
