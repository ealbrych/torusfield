from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
import numpy as np

#fig = plt.figure(figsize = (6, 6))
fig = plt.figure(figsize = (6, 6))
#ax = fig.gca(projection='3d')
ax = fig.add_subplot(1,1,1, projection = '3d')

# Make the grid
x, y, z = np.meshgrid(np.arange(-2.0, 2.2, 0.5),
                      np.arange(-2.0, 2.2, 0.5),
                      np.arange(-2.0, 2.2, 0.5))

q1 = 1
q2 = -1
dist = 2

axcolor = 'lightgoldenrodyellow'
acharge1 = plt.axes([0.25, 0.01, 0.65, 0.03], facecolor=axcolor)
charge1 = Slider(acharge1, 'Charge 1', -2.0, 2.0, valinit=q1)
acharge2 = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor=axcolor)
charge2 = Slider(acharge2, 'Charge 2', -2.0, 2.0, valinit=q2)


# Make the direction data for the arrows
u1 = q1*x/(x**2+y**2+(z-dist/2)**2)**(3/2) 
u2 = q2*x/(x**2+y**2+(z+dist/2)**2)**(3/2)
v1 = q1*y/(x**2+y**2+(z-dist/2)**2)**(3/2) 
v2 = q2*y/(x**2+y**2+(z+dist/2)**2)**(3/2)
w1 = q1*(z-dist/2)/(x**2+y**2+(z-dist/2)**2)**(3/2) 
w2 = q2*(z+dist/2)/(x**2+y**2+(z+dist/2)**2)**(3/2)

u=u1+u2
v=v1+v2
w=w1+w2

ax.quiver(x, y, z, u, v, w, length=0.2)

def update(val):
    q1n = charge1.val
    q2n = charge2.val
    ax.clear()
    #u = q1n*x/(x**2+y**2+(z-dist/2)**2)**(3/2) + q2n*x/(x**2+y**2+(z+dist/2)**2)**(3/2)
    #v = q1n*y/(x**2+y**2+(z-dist/2)**2)**(3/2) + q2n*y/(x**2+y**2+(z+dist/2)**2)**(3/2)
    #w = q1n*(z-dist/2)/(x**2+y**2+(z-dist/2)**2)**(3/2) + q2n*(z+dist/2)/(x**2+y**2+(z+dist/2)**2)**(3/2)
    ax.quiver(x, y, z, q1n*u1+q2n*u2, q1n*v1+q2n*v2, q1n*w1+q2n*w2, length=0.05)
    ax.set_aspect('equal')
    ax.scatter(0,0,1, s=40, c='red')
    ax.scatter(0,0,-1, s=40, c='blue')
    ax.set_aspect('equal')
    ax.auto_scale_xyz([-2.0, 2.0], [-2.0, 2.0], [-2.0, 2.0])
    fig.canvas.draw_idle()
    #fig.draw()
charge1.on_changed(update)
charge2.on_changed(update)


ax.scatter(0,0,1, s=40, c='red')
ax.scatter(0,0,-1, s=40, c='blue')

ax.set_aspect('equal')
ax.auto_scale_xyz([-2.0, 2.0], [-2.0, 2.0], [-2.0, 2.0])

plt.show()