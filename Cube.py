from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize = (6, 6))
ax = fig.gca(projection='3d')

# Make the grid
a = np.arange(-1, 1.1, 0.4)
b = np.arange(-1, 1.1, 0.4)
c = np.arange(-1, 1.1, 0.4)
i, j, k = np.meshgrid(a, b, c)

q = 1

xside = 1
yside = 1
zside = 1

xstep = 10
ystep = 10
zstep = 10

outside = (i < -xside/2) | (i > xside/2) | (j < -yside/2) | (j > yside/2) | (k < -zside/2) | (k > zside/2)

x = i[outside]
y = j[outside]
z = k[outside]

def u(x,y,z):
    x_sum = 0
    for a in np.arange(-xside/2,xside/2, xside/xstep):
        for b in np.arange(-yside/2,yside/2, yside/ystep):
            for c in np.arange(-zside/2,zside/2, zside/zstep):
                x_sum += q / (xstep * ystep * zstep) * (x-a)/((x-a)**2+(y-b)**2+(z-c)**2)**(3/2)
    return x_sum
def v(x,y,z):
    y_sum = 0
    for a in np.arange(-xside/2,xside/2, xside/xstep):
        for b in np.arange(-yside/2,yside/2, yside/ystep):
            for c in np.arange(-zside/2,zside/2, zside/zstep):
                y_sum += q / (xstep * ystep * zstep) * (y-b)/((x-a)**2+(y-b)**2+(z-c)**2)**(3/2)
    return y_sum
def w(x,y,z):
    z_sum = 0
    for a in np.arange(-xside/2,xside/2, xside/xstep):
        for b in np.arange(-yside/2,yside/2, yside/ystep):
            for c in np.arange(-zside/2,zside/2, zside/zstep):
                z_sum += q / (xstep * ystep * zstep) * (z-c)/((x-a)**2+(y-b)**2+(z-c)**2)**(3/2)
    return z_sum

# Make the direction data for the arrows
u = u(x,y,z)
v = v(x,y,z)
w = w(x,y,z)

ax.quiver(x, y, z, u, v, w, length=0.1)

ax.set_aspect('equal')
ax.auto_scale_xyz([-1.0, 1.0], [-1.0, 1.0], [-1.0, 1.0])

plt.show()