from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection

fig = plt.figure(figsize = (6, 6))
ax = fig.gca(projection='3d')


# ----- CHARGE PARAMETERS -----
q = 1                  # total charge

radius = 1

step_size = 0.1        # size of step

# ----- WINDOW PARAMETERS -----
window_size = 1        # window extends from -window_size to window_size

# ----- VECTOR PARAMETERS -----
vector_spacing = 0.4   # distance between vectors
arrow_length = 0.05     # length scale for arrows

# ----- VECTOR PLOT -----

# Make the grid
a = np.arange(-window_size, window_size+0.1, vector_spacing)
b = np.arange(-window_size, window_size+0.1, vector_spacing)
c = np.arange(-window_size, window_size+0.1, vector_spacing)
i, j, k = np.meshgrid(a, b, c)

# Remove object volume from meshgrid
outside = np.sqrt(i**2 + j**2 + k**2) > radius

x = i[outside]
y = j[outside]
z = k[outside]

density = q / (4/3*np.pi*radius**3)

# Calculate vector using integration
def V(x, y, z):
    x_sum = 0
    y_sum = 0
    z_sum = 0
    for a in np.arange(-radius,radius, step_size):
        for b in np.arange(-np.sqrt(radius**2 - a**2), np.sqrt(radius**2 - a**2), step_size):
            for c in np.arange(-np.sqrt(abs(radius**2 - a**2 - b**2)), np.sqrt(abs(radius**2 - a**2 - b**2)), step_size):
                x_sum += density * step_size**3  * (x-a)/((x-a)**2+(y-b)**2+(z-c)**2)**(3/2)
                y_sum += density * step_size**3 * (y-b)/((x-a)**2+(y-b)**2+(z-c)**2)**(3/2)
                z_sum += density * step_size**3 * (z-c)/((x-a)**2+(y-b)**2+(z-c)**2)**(3/2)
    return [x_sum, y_sum, z_sum]

# Make the direction data for the arrows
V = V(x, y, z)
u = V[0]
v = V[1]
w = V[2]

ax.quiver(x, y, z, u, v, w, length=arrow_length)

ax.set_aspect('equal')
ax.auto_scale_xyz([-window_size, window_size], [-window_size, window_size], [-window_size, window_size])

plt.show()