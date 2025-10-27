import matplotlib.pyplot as plt
import numpy as np
def neg_damping(a, V):

    A = 100000
    print
    return (2*1.204*V*A*(5*a+2))/(3*a-1)

A = np.linspace(0.1, 0.5, 33)
Vs = np.linspace(5, 25, 33)
print((2*1.204*12*10000*(5*0.4+2))/(3*0.2-1))

plt.plot(A, neg_damping(A, 12))
plt.xlabel('Axial induction factor')
plt.ylabel('Negative damping (N/(m/s))')
plt.title('Effect of axial inductin factor on negative damping')




results = np.zeros((33, 33))
for i, a in enumerate(A):
    for j, v in enumerate(Vs):
        results[i, j] = neg_damping(a, v)
        
plt.figure()
plt.contourf(A, Vs, results, 50)
plt.colorbar()
plt.show()