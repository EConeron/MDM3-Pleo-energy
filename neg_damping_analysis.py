import matplotlib.pyplot as plt
import numpy as np
def neg_damping(a, V):
    '''
    Function to calcualte the negative damping from the mathematical equation
    '''

    # Area of turbine blades
    A = np.pi * 125**2

    return (2*1.204*V*A*(5*a+2))/(3*a-1)

# Values of axial induction factors
A = np.linspace(0.1, 0.5,41 )

plt.plot(A, neg_damping(A, 12))
plt.xlabel('Axial induction factor')
plt.ylabel('Negative damping (N/(m/s))')
plt.title('Effect of axial induction factor on negative damping')
plt.grid()
plt.show()
plt.savefig('Negdamping')


