from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection

fig = plt.figure(figsize = (6, 6))
ax = fig.gca(projection='3d')


# ----- CHARGE PARAMETERS -----
q = 1                  # total charge

xside = 0.1              # prism side lengths
yside = 0.1
zside = 2

xstep = 20             # number of divisons for integration
ystep = 20
zstep = 20

# ----- WINDOW PARAMETERS -----
window_size = 1        # window extends from -window_size to window_size

# ----- VECTOR PARAMETERS -----
vector_spacing = 0.4   # distance between vectors
arrow_length = 0.2     # length scale for arrows

# ----- GRAPHICS FOR CUBE -----
def plot_cube(cube_definition):
    cube_definition_array = [
        np.array(list(item))
        for item in cube_definition
    ]

    points = []
    points += cube_definition_array
    vectors = [
        cube_definition_array[1] - cube_definition_array[0],
        cube_definition_array[2] - cube_definition_array[0],
        cube_definition_array[3] - cube_definition_array[0]
    ]

    points += [cube_definition_array[0] + vectors[0] + vectors[1]]
    points += [cube_definition_array[0] + vectors[0] + vectors[2]]
    points += [cube_definition_array[0] + vectors[1] + vectors[2]]
    points += [cube_definition_array[0] + vectors[0] + vectors[1] + vectors[2]]

    points = np.array(points)

    edges = [
        [points[0], points[3], points[5], points[1]],
        [points[1], points[5], points[7], points[4]],
        [points[4], points[2], points[6], points[7]],
        [points[2], points[6], points[3], points[0]],
        [points[0], points[2], points[4], points[1]],
        [points[3], points[6], points[7], points[5]]
    ]

    faces = Poly3DCollection(edges, linewidths=1, edgecolors='k')
    faces.set_facecolor((1,1,0,0.2))

    ax.add_collection3d(faces)

    # Plot the points themselves to force the scaling of the axes
    ax.scatter(points[:,0], points[:,1], points[:,2], s=0)

cube_definition = [
    (-xside/2,-yside/2,-zside/2), (-xside/2,yside/2,-zside/2), (xside/2,-yside/2,-zside/2), (-xside/2,-yside/2,zside/2)
]
plot_cube(cube_definition)

# ----- VECTOR PLOT -----

# Make the grid
a = np.arange(-window_size, window_size+0.1, vector_spacing)
b = np.arange(-window_size, window_size+0.1, vector_spacing)
c = np.arange(-window_size, window_size+0.1, vector_spacing)
i, j, k = np.meshgrid(a, b, c)

# Remove object volume from meshgrid
outside = (i < -xside/2) | (i > xside/2) | (j < -yside/2) | (j > yside/2) | (k < -zside/2) | (k > zside/2)

x = i[outside]
y = j[outside]
z = k[outside]

# Calculate vector using integration
def V(x, y, z):
    x_sum = 0
    y_sum = 0
    z_sum = 0
    for a in np.arange(-xside/2,xside/2, xside/xstep):
        for b in np.arange(-yside/2,yside/2, yside/ystep):
            for c in np.arange(-zside/2,zside/2, zside/zstep):
                x_sum += q / (xstep * ystep * zstep) * (x-a)/((x-a)**2+(y-b)**2+(z-c)**2)**(3/2)
                y_sum += q / (xstep * ystep * zstep) * (y-b)/((x-a)**2+(y-b)**2+(z-c)**2)**(3/2)
                z_sum += q / (xstep * ystep * zstep) * (z-c)/((x-a)**2+(y-b)**2+(z-c)**2)**(3/2)
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