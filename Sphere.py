from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
import numpy as np


fig = plt.figure(figsize = (6, 6))
ax = fig.gca(projection='3d')


# ----- CHARGE PARAMETERS -----
q = 1                  # total charge

radius = 0.5

step_size = 0.1        # size of step

# ----- WINDOW PARAMETERS -----
window_size = 1        # window extends from -window_size to window_size

# ----- VECTOR PARAMETERS -----
vector_spacing = 0.4   # distance between vectors
arrow_length = 0.2     # length scale for arrows

# draw sphere
u, v = np.mgrid[0:2*np.pi:40j, 0:np.pi:40j]
x = radius*np.cos(u)*np.sin(v)
y = radius*np.sin(u)*np.sin(v)
z = radius*np.cos(v)
ax.plot_wireframe(x, y, z, color="r")

# animation slider
axcolor = 'lightgoldenrodyellow'
acharge = plt.axes([0.25, 0.01, 0.65, 0.03], facecolor=axcolor)
charge = Slider(acharge, 'Charge', -2.0, 2.0, valinit=q)
ar = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor=axcolor)
r = Slider(ar, 'Radius', 0.01, 0.96, valinit=radius)


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


# Calculate vector using integration
def field(x, y, z, q):
    density = q / (4/3*np.pi*radius**3)
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
V = field(x, y, z, q)
u = V[0]
v = V[1]
w = V[2]

ax.quiver(x, y, z, u, v, w, length=arrow_length)

# animation update                            
def update(val):
    qn = charge.val
    rn = r.val
    ax.clear()
    a = np.arange(-window_size, window_size+0.1, vector_spacing)
    b = np.arange(-window_size, window_size+0.1, vector_spacing)
    c = np.arange(-window_size, window_size+0.1, vector_spacing)
    i, j, k = np.meshgrid(a, b, c)

    outside = np.sqrt(i**2 + j**2 + k**2) > rn

    x = i[outside]
    y = j[outside]
    z = k[outside]
    V = field(x, y, z, qn)
    ax.quiver(x, y, z, V[0], V[1], V[2], length=0.1)
    ax.set_aspect('equal')  
    ax.auto_scale_xyz([-1.0, 1.0], [-1.0, 1.0], [-1.0, 1.0])
    u, v = np.mgrid[0:2*np.pi:40j, 0:np.pi:40j]
    l = rn*np.cos(u)*np.sin(v)
    m = rn*np.sin(u)*np.sin(v)
    n = rn*np.cos(v)
    ax.plot_wireframe(l, m, n, color="r")

    fig.canvas.draw_idle()
    #fig.draw()
charge.on_changed(update) 
r.on_changed(update) 

ax.set_aspect('equal')

plt.show()