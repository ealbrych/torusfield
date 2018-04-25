from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize = (6, 6))
ax = fig.gca(projection='3d')


# ----- CHARGE PARAMETERS -----
q = 1                  # total charge

a = 0.5
b = 0.2

step_size_r = 0.04        # size of step
step_size_theta = 2*np.pi/100
step_size_h = 0.04

# ----- WINDOW PARAMETERS -----
window_size = 1        # window extends from -window_size to window_size

# ----- VECTOR PARAMETERS -----
vector_spacing = 0.5   # distance between vectors
arrow_length = 0.1     # length scale for arrows

# draw torus
u, v = np.mgrid[0:2*np.pi:20j, 0:2*np.pi:20j]
x = np.cos(u) * (a + b*np.cos(v))
y = np.sin(u) * (a + b*np.cos(v))
z = b*np.sin(v)
ax.plot_wireframe(x, y, z, color="r")

# ----- VECTOR PLOT -----

# Make the grid
l = np.arange(-window_size, window_size+0.1, vector_spacing)
m = np.arange(-window_size, window_size+0.1, vector_spacing)
n = np.arange(-window_size, window_size+0.1, vector_spacing)
i, j, k = np.meshgrid(l, m, n)

# Remove object volume from meshgrid
outside = np.sqrt((np.sqrt(i**2 + j**2) - a)**2 + k**2) > b

x = i[outside]
y = j[outside]
z = k[outside]

density = q / (np.pi**2 * 2 * b**2 * a)

# Calculate vector using integration
def V(x, y, z):
    x_sum = 0
    y_sum = 0
    z_sum = 0
    for h in np.arange(-b, b, step_size_h):
        for theta in np.arange(0, 2*np.pi, step_size_theta):
            for r in np.arange(a-np.sqrt(b**2-h**2), a+np.sqrt(b**2-h**2), step_size_r):
                x_sum += density * step_size_h * step_size_r * step_size_theta * r * (x-r*np.cos(theta))/((x-r*np.cos(theta))**2+(y-r*np.sin(theta))**2+(z-h)**2)**(3/2)
                y_sum += density * step_size_h * step_size_r * step_size_theta * r * (y-r*np.sin(theta))/((x-r*np.cos(theta))**2+(y-r*np.sin(theta))**2+(z-h)**2)**(3/2)
                z_sum += density * step_size_h * step_size_r * step_size_theta * r * (z-h)/((x-r*np.cos(theta))**2+(y-r*np.sin(theta))**2+(z-h)**2)**(3/2)
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