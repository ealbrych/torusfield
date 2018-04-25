from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize = (6, 6))
ax = fig.gca(projection='3d')


# ----- CHARGE PARAMETERS -----
q = 1                  # total charge

b = 0.2
a = 0.5

step_size = 0.01        # size of step

# ----- WINDOW PARAMETERS -----
window_size = 1        # window extends from -window_size to window_size

# ----- VECTOR PARAMETERS -----
vector_spacing = 0.4   # distance between vectors
arrow_length = 0.2     # length scale for arrows



# ----- VECTOR PLOT -----

# Make the grid
l = np.arange(-window_size, window_size+0.1, vector_spacing)
m = np.arange(-window_size, window_size+0.1, vector_spacing)
n = np.arange(-window_size, window_size+0.1, vector_spacing)
i, j, k = np.meshgrid(l, m, n)

x=i
y=j
z=k

density = q / (np.pi**2 * 2 * b**2 * a)

# Calculate vector using integration
def V(x, y, z):
    x_sum = 0
    y_sum = 0
    z_sum = 0
    for h in np.arange(-b, b, step_size):
        for theta in np.arange(0, 2*np.pi, step_size):
            for r in np.arange(a-np.sqrt(b**2-h**2), a+np.sqrt(b**2-h**2), step_size):
                x_sum += density * step_size**3  * r * (x-r*np.cos(theta))/((x-r*np.cos(theta))**2+(y-r*np.sin(theta))**2+(z-h)**2)**(3/2)
                y_sum += density * step_size**3 * r * (y-r*np.sin(theta))/((x-r*np.cos(theta))**2+(y-r*np.sin(theta))**2+(z-h)**2)**(3/2)
                z_sum += density * step_size**3 * r * (z-h)/((x-r*np.cos(theta))**2+(y-r*np.sin(theta))**2+(z-h)**2)**(3/2)
    return [x_sum, y_sum, z_sum]

# Make the direction data for the arrows
V = V(x, y, z)
u = V[0]
v = V[1]
w = V[2]

ax.quiver(x, y, z, u, v, w, length=arrow_length)

ax.set_xlim3d([-window_size, window_size])
ax.set_ylim3d([-window_size, window_size])
ax.set_zlim3d([-window_size, window_size])

ax.set_aspect('equal')

plt.show()