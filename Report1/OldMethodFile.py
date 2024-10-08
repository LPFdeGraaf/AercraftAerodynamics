import numpy as np
import matplotlib.pyplot as plt

#   nput Camber line
c = 1.
alpha = 9
alpha_plate = 0
N = 60 #   Number of sections + 1
dl = c / (N-1)



points = np.linspace(0, c, N) # N Subpanel points
vort_points = points[1:] - 3./4 * dl #   Quarter chord points
col_points = points[1:] - 1./4 * dl # Three-Quarter chord points


#   Flat plat; flat plate inclination
alpha_i = np.ones(N-1)*alpha_plate

#   Quarter chord points, normal and tangential vectors
xj = np.cos(np.deg2rad(alpha_i)) * vort_points
zj = np.sin(np.deg2rad(alpha_i)) * vort_points

# Three-quarter chord points, normal and tangential vectors
xi = np.cos(np.deg2rad(alpha_i)) * col_points
zi = np.sin(np.deg2rad(alpha_i)) * col_points
ni = np.vstack((np.sin(np.deg2rad(alpha_i)), np.cos(np.deg2rad(alpha_i))))
ti = np.vstack((np.cos(np.deg2rad(alpha_i)), -np.sin(np.deg2rad(alpha_i))))


plt.plot(np.cos(np.deg2rad(alpha)) * points, np.sin(np.deg2rad(alpha)) * points, 'x')
plt.plot(xj, zj, 'x')
plt.plot(xi, zi, 'o')
plt.grid(True)
plt.show()



def vort2D(x, z, xjj, zjj):
    # Gamma_i is of unit strenght for now
    rj2 = (x - xjj)**2 + (z - zjj)**2
    B = np.array([1*(z - zjj), -1 * (x - xjj)])
    C = 1/(2*np.pi*rj2) * B
    return C


aij = np.zeros((N-1, N-1))

for i in range(N-1):  # Three-quarter chord points loop
    for j in range(N-1):  # Quarter chord points loop

        # aij is correct according to the LHS of eq. 11.7 in Katz
        aij[i,j] = np.inner(vort2D(xi[i], zi[i], xj[j], zj[j]), ni[:, i])


# print(aij*np.pi * dl)


#   Missing the Qinf here on the right hand side
RHSi = np.cos(np.deg2rad(alpha)) * np.sin(np.deg2rad(alpha_i)) + np.sin(np.deg2rad(alpha)) * np.cos(np.deg2rad(alpha_i))
#   Gamma_i is consistent the example of 5 sections in Katz 11.1.1
Gamma_i = np.linalg.solve(aij, -RHSi)
print(Gamma_i / dl / np.pi/ np.sin(np.deg2rad(alpha)))

# print(np.allclose(np.dot(aij, Gamma_i), -RHSi))





#   Chordwise pressure coefficient
delcpi = 2. * Gamma_i / dl


#   Analytical test case?

An_delcp = 4. * np.sqrt((1. - xj)/xj) * alpha/180 * np.pi


plt.plot(xj, delcpi, label='Delcpi')
plt.plot(xj, An_delcp, label='An_delcp')
plt.legend(loc='best')

plt.grid(True)
plt.xlim([0, c])
#plt.ylim(max(delL), min(delL))
plt.show()


plt.plot(xj, An_delcp, label='An_delcp')
plt.show()
