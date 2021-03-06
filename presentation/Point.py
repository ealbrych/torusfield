from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
import numpy as np

#fig = plt.figure(figsize = (6, 6))
fig = plt.figure(figsize = (6, 6))
#ax = fig.gca(projection='3d')
ax = fig.add_subplot(1,1,1, projection = '3d')
q0=1
axcolor = 'lightgoldenrodyellow'
axamp = plt.axes([0.25, 0.01, 0.65, 0.03], facecolor=axcolor)
samp = Slider(axamp, 'Charge', -2.0, 2.0, valinit=q0)




# Make the grid
x, y, z = np.meshgrid(np.arange(-1, 1.2, 0.4),
                      np.arange(-1, 1.2, 0.4),
                      np.arange(-1, 1.2, 0.4))

# Make the direction data for the arrows
u = q0*x/(x**2+y**2+z**2)**(3/2)
v = q0*y/(x**2+y**2+z**2)**(3/2)
w = q0*z/(x**2+y**2+z**2)**(3/2)

ax.quiver(x, y, z, u, v, w, length=0.05)

def update(val):
    q = samp.val
    ax.clear()
    ax.quiver(x, y, z, q*u, q*v, q*w, length=0.05)
    ax.set_aspect('equal')
    
    hue = int(90.15 * np.sqrt(abs(q)) + 128)
    hue_str = str(hex(hue))[2:]
    sat = int(128 - abs(64 * q))
    sat_str = str(hex(sat))[2:]
    if sat < 16:
        sat_str = '0' + sat_str
    
    if q >= 0:
        ax.scatter(0,0,0, s=40, c='#' + hue_str + sat_str + sat_str)
    elif q < 0:
        ax.scatter(0,0,0, s=40, c='#' + sat_str + sat_str + hue_str)
        
    ax.auto_scale_xyz([-1.0, 1.0], [-1.0, 1.0], [-1.0, 1.0])
    fig.canvas.draw_idle()
    #fig.draw()
samp.on_changed(update)

ax.scatter(0,0,0, s=40, c='#DA4040')

ax.set_aspect('equal')
ax.auto_scale_xyz([-1.0, 1.0], [-1.0, 1.0], [-1.0, 1.0])

plt.show()