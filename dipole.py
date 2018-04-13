from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize = (6, 6))
ax = fig.gca(projection='3d')

# Make the grid
x, y, z = np.meshgrid(np.arange(-2.0, 2.2, 0.8),
                      np.arange(-2.0, 2.2, 0.8),
                      np.arange(-2.0, 2.2, 0.8))

# Make the direction data for the arrows
u = x/(x**2+y**2+(z-1)**2)**(3/2)-x/(x**2+y**2+(z+1)**2)**(3/2)
v = y/(x**2+y**2+(z-1)**2)**(3/2)-y/(x**2+y**2+(z+1)**2)**(3/2)
w = (z-1)/(x**2+y**2+(z-1)**2)**(3/2)-(z+1)/(x**2+y**2+(z+1)**2)**(3/2)

ax.quiver(x, y, z, u, v, w, length=0.2)

ax.scatter(0,0,1, s=40, c='red')
ax.scatter(0,0,-1, s=40, c='blue')

ax.set_aspect('equal')
ax.auto_scale_xyz([-2.0, 2.0], [-2.0, 2.0], [-2.0, 2.0])

plt.show()