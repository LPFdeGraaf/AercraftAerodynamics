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

# Experimental pressure coefficients Naca 0012 at AOA = 15

# Column 1: x/c
x_c_15 = np.array(
    [-7.59438e-05, 0.0024302, 0.00450442, 0.00870506, 0.0129722, 0.0167741, 0.0467387, 0.0769928, 0.0964534,
     0.146315, 0.174528, 0.287443, 0.317853, 0.380854, 0.443854, 0.509042, 0.576404, 0.635076, 0.698095, 0.761123,
     0.8285, 0.893707, 0.954576, 1.00022])

# Column 2: cp
cp_15 = np.array(
    [-8.65066, -10.1789, -9.72033, -9.04329, -8.67192, -6.16084, -3.99796, -3.16694, -2.68574, -2.05038, -1.83081,
     -1.23636, -1.12586, -0.9266, -0.727343, -0.593492, -0.459546, -0.347813, -0.235891, -0.167637, -0.0991921,
     -0.0526765, -0.0500185, -0.00435728])

# from https: // turbmodels.larc.nasa.gov / naca0012_val.html
# Essentially from the 'Theory of wing sections'
# Column 1: alpha, deg
alpha_deg = np.array([-17.2794, -16.2296, -15.8616, -15.1713, -14.3133, -13.2811, -12.2535, -11.2222, -10.1947, -8.14138,
             -6.25579, -5.22822, -4.19972, -1.96944, 0.0, 0.940006, 1.96944, 2.99515, 3.85131, 4.87888, 5.90831,
             7.96346, 10.1891, 11.0471, 13.1088, 16.3759, 16.5678, 17.2971])

# Column 2: cl
cl = np.array([-1.25323, -1.34704, -1.54416, -1.51805, -1.44038, -1.3712, -1.25912, -1.18135, -1.06927, -0.827958, -0.638207,
      -0.526128, -0.422627, -0.215533, 0.0, 0.120611, 0.215533, 0.34477, 0.439599, 0.551678, 0.6466, 0.870758,
      1.12074, 1.19842, 1.36252, 1.59591, 1.42443, 1.09024])


class DiscreteVortexMethod:

    def __init__(self, alpha, alpha_plate, subpanels):
        self.alpha = alpha
        self.alpha_i = np.ones(subpanels) * alpha_plate
        self.subpanels = subpanels
        self.dl = 1. / subpanels

    def GridGeneration(self):
        points = np.linspace(0, 1., self.subpanels + 1)
        vort_points = points[1:] - 3./4 * self.dl
        col_points = points[1:] - 1./4 * self.dl

        #   Quarter chord points
        xj = np.cos(np.deg2rad(self.alpha_i)) * vort_points
        zj = np.sin(np.deg2rad(self.alpha_i)) * vort_points

        # Three-quarter chord points, normal and tangential vectors
        xi = np.cos(np.deg2rad(self.alpha_i)) * col_points
        zi = np.sin(np.deg2rad(self.alpha_i)) * col_points
        ni = np.vstack((np.sin(np.deg2rad(self.alpha_i)), np.cos(np.deg2rad(self.alpha_i))))

        # plt.plot(np.cos(np.deg2rad(alpha)) * points, np.sin(np.deg2rad(alpha)) * points, 'x')
        # plt.plot(xj, zj, 'x')
        # plt.plot(xi, zi, 'o')
        # plt.grid(True)
        # plt.show()

        return xi, zi, xj, zj, ni

    def Vort2D(self, xi, zi,  xj, zj):
        # Gamma_i is of unit strength for now
        rj2 = (xi - xj) ** 2 + (zi - zj) ** 2
        B = np.array([1 * (zi - zj), -1 * (xi - xj)])
        C = 1 / (2 * np.pi * rj2) * B
        return C


    def Calc_delta_Cp(self, xi, zi, xj, zj, ni):
        aij = np.zeros((self.subpanels, self.subpanels))

        for i in range(self.subpanels):
            for j in range(self.subpanels):
                aij[i, j] = np.inner(self.Vort2D(xi[i], zi[i], xj[j], zj[j]), ni[:, i])

        RHSi = np.cos(np.deg2rad(self.alpha)) * np.sin(np.deg2rad(self.alpha_i)) +  np.sin(np.deg2rad(self.alpha)) *  np.cos(np.deg2rad(self.alpha_i))
        Gamma_i = np.linalg.solve(aij, -RHSi) #   Gamma_i is consistent the example of 5 sections in Katz 11.1.1
        delcpi = 2. * Gamma_i / self.dl #   Chordwise pressure coefficient

        return Gamma_i, delcpi

    def lift_coeff(self, Gamma_i):
        Cl = 2 * np.sum(Gamma_i)
        print('Lift coefficient is {}'.format(Cl))
        return Cl
    def plot_results(self, xj, delcpi):
        An_delcp = 4. * np.sqrt((1. - xj) / xj) * self.alpha / 180 * np.pi
        plt.ylabel(r'$\Delta$')
        plt.xlabel(R'$x/c$')
        plt.plot(xj, delcpi, label=r'H')
        plt.plot(xj, An_delcp, label='An_delcp')
        if self.alpha == 10:
            plt.plot(x_c_10, np.abs(cp_10), label='Exp. Data', linestyle = '--')
        if self.alpha == 15:
            plt.plot(x_c_15, np.abs(cp_15), label='Exp. Data')
        plt.legend(loc='best')
        plt.grid(True)
        plt.xlim([0, 1.])
        plt.ylim([0, np.max((delcpi, An_delcp))])
        #plt.savefig("CP_alpha{}.png".format(self.alpha))
        plt.show()


def CL_alpha_curve(alpha, alpha_plate, subpanels):
    Cl = []
    alphalist = np.ones(alpha)

    for i in range(alpha):
        vortex_method = DiscreteVortexMethod(i, alpha_plate, subpanels)
        xi, zi, xj, zj, ni = vortex_method.GridGeneration()
        Gamma_i, delcpi = vortex_method.Calc_delta_Cp(xi, zi, xj, zj, ni)
        vortex_method.plot_results(xj, delcpi)
        Cl.append(vortex_method.lift_coeff(Gamma_i))
        alphalist[i] = i

    plt.plot(alphalist, Cl, label='Lift coefficient')
    plt.plot(alphalist, 2 * np.pi * alphalist / 180 * np.pi, label='2 piefficient')
    plt.plot(alpha_deg, cl)
    plt.xlim([-2, 12])
    plt.ylim([-0.1, 1.1])
    plt.show()

if __name__ == "__main__":
    c = 1.0             # Chord length
    alpha = 15         # Angle of attack
    alpha_plate = 0.    # Inclination of the plate
    subpanels = 60      # Number of subpanels


    # Method
    vortex_method = DiscreteVortexMethod(alpha, alpha_plate, subpanels)
    xi, zi, xj, zj, ni = vortex_method.GridGeneration()
    Gamma_i, delcpi = vortex_method.Calc_delta_Cp(xi, zi, xj, zj, ni)
    vortex_method.plot_results(xj, delcpi)


    #   Plotting the Cl curves
    #CL_alpha_curve(alpha, alpha_plate, subpanels)






