import numpy as np
import matplotlib.pyplot as plt


# Experimental pressure coefficients Naca 0012 at AOA = 10

# Column 1: x/c
x_c_10 = np.array(
    [0.0, 0.00218341, 0.00873362, 0.0131004, 0.0174672, 0.0480349, 0.0742358, 0.0982533, 0.124454, 0.146288,
     0.176856, 0.28821, 0.320961, 0.384279, 0.447598, 0.515284, 0.576419, 0.637555, 0.700873, 0.766376, 0.831878,
     0.893013, 0.958515, 1.0])

# Column 2: cp
cp_10 = np.array(
    [-3.66423, -5.04375, -5.24068, -4.67125, -4.32079, -2.74347, -2.26115, -1.95405, -1.7345, -1.55884, -1.36109,
     -1.00829, -0.941877, -0.787206, -0.654432, -0.543461, -0.432633, -0.343703, -0.254725, -0.1657, -0.098572,
     -0.00964205, 0.0793835, 0.124088])


plt.plot(x_c_10, np.abs(cp_10), label='Exp. Data', linestyle = '--')
plt.xlabel('\latex')
plt.show()