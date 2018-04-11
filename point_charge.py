from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize = (6, 6))
ax = fig.gca(projection='3d')

# Make the grid
x, y, z = np.meshgrid(np.arange(-1, 1.2, 0.4),
                      np.arange(-1, 1.2, 0.4),
                      np.arange(-1, 1.2, 0.4))



# Make the direction data for the arrows

u = x/(x**2+y**2+z**2)**(3/2)

v = y/(x**2+y**2+z**2)**(3/2)

w = z/(x**2+y**2+z**2)**(3/2)



ax.quiver(x, y, z, u, v, w, length=0.05)

ax.set_aspect('equal')

ax.auto_scale_xyz([-1.0, 1.0], [-1.0, 1.0], [-1.0, 1.0])



plt.show()

