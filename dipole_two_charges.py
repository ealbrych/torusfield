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

def field(x, y, z, q1, q2, dist):
    u1 = x/(x**2+y**2+(z-dist/2)**2)**(3/2) 
    u2 = x/(x**2+y**2+(z+dist/2)**2)**(3/2)
    v1 = y/(x**2+y**2+(z-dist/2)**2)**(3/2) 
    v2 = y/(x**2+y**2+(z+dist/2)**2)**(3/2)
    w1 = (z-dist/2)/(x**2+y**2+(z-dist/2)**2)**(3/2) 
    w2 = (z+dist/2)/(x**2+y**2+(z+dist/2)**2)**(3/2)
    
    u = q1*u1+q2*u2
    v = q1*v1+q2*v2
    w = q1*w1+q2*w2
    
    no_show = np.sqrt(u**2 + v**2 + w**2) > 15
    
    u[no_show] = 0
    v[no_show] = 0
    w[no_show] = 0
    
    return [u, v, w]

axcolor = 'lightgoldenrodyellow'
acharge1 = plt.axes([0.25, 0.01, 0.65, 0.03], facecolor=axcolor)
charge1 = Slider(acharge1, 'Charge 1', -2.0, 2.0, valinit=q1)
acharge2 = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor=axcolor)
charge2 = Slider(acharge2, 'Charge 2', -2.0, 2.0, valinit=q2)
adistance = plt.axes([0.25, 0.09, 0.65, 0.03], facecolor=axcolor)
distance = Slider(adistance, 'Distance', 0.0, 4.0, valinit=dist)


# Make the direction data for the arrows
V = field(x, y, z, q1, q2, dist)
ax.quiver(x, y, z, V[0], V[1], V[2], length=0.1)

def update(val):
    q1n = charge1.val
    q2n = charge2.val
    distn = distance.val
    ax.clear()
    
    V = field(x, y, z, q1n, q2n, distn)
    ax.quiver(x, y, z, V[0], V[1], V[2], length=0.1)
    ax.set_aspect('equal')
    
    hue1 = int(90.15 * np.sqrt(abs(q1n)) + 128)
    hue2 = int(90.15 * np.sqrt(abs(q2n)) + 128)
    
    hue_str1 = str(hex(hue1))[2:]
    hue_str2 = str(hex(hue2))[2:]
    
    sat1 = int(128 - abs(64 * q1n))
    sat2 = int(128 - abs(64 * q2n))
    
    sat_str1 = str(hex(sat1))[2:]
    if sat1 < 16:
        sat_str1 = '0' + sat_str1
        
    sat_str2 = str(hex(sat2))[2:]
    if sat2 < 16:
        sat_str2 = '0' + sat_str2
    
    opacity1 = int(abs(63.5 * q1n) + 128)
    opacity2 = int(abs(63.5 * q2n) + 128)
    
    opacity_str1 = str(hex(opacity1))[2:]
    opacity_str2 = str(hex(opacity2))[2:]
    
    if q1n >= 0:
        ax.scatter(0,0,distn/2, s=40, c='#' + hue_str1 + sat_str1 + sat_str1 + opacity_str1)
    elif q1n < 0:
        ax.scatter(0,0,distn/2, s=40, c='#' + sat_str1 + sat_str1 + hue_str1 + opacity_str1)
    if q2n >= 0:
        ax.scatter(0,0,-distn/2, s=40, c='#' + hue_str2 + sat_str2 + sat_str2 + opacity_str2)
    elif q2n < 0:
        ax.scatter(0,0,-distn/2, s=40, c='#' + sat_str2 + sat_str2 + hue_str2 + opacity_str2)

    ax.set_aspect('equal')
    ax.auto_scale_xyz([-2.0, 2.0], [-2.0, 2.0], [-2.0, 2.0])
    fig.canvas.draw_idle()
    #fig.draw()
charge1.on_changed(update)
charge2.on_changed(update)
distance.on_changed(update)


ax.scatter(0,0,1, s=40, c='#DA4040BF')
ax.scatter(0,0,-1, s=40, c='#4040DABF')

ax.set_aspect('equal')
ax.auto_scale_xyz([-2.0, 2.0], [-2.0, 2.0], [-2.0, 2.0])

plt.show()