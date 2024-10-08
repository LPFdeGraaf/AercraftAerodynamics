import numpy as np
import matplotlib.pyplot as plt


path = '/home/zbook/Desktop/MSc/Q1/AercraftAerodynamics/Report2/'
part1 = 'Part 1/'
airfoil = np.loadtxt(path + part1 + 'myairfoil.txt', skiprows=1)

plt.plot(airfoil[:,0], airfoil[:,1], label='Airfoil')
plt.grid(True)
plt.axis('equal')
plt.ylim([-0.2, 0.2])
plt.ylabel('t/c [-]')
plt.xlabel('x\c [-] ')
plt.show()

