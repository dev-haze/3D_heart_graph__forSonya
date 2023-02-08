import numpy as np
from matplotlib import pyplot as plt

ax = plt.figure().add_subplot(projection='3d')
plt.ylim([-25, 25])

def heart3(size,loc):
    theta = np.linspace(-2 * np.pi, 2 * np.pi, 100)
    z = (13*np.cos(theta)-5*np.cos(2*theta)-2*np.cos(3*theta)-np.cos(4*theta))*size
    x = (16*(np.sin(theta)**3))*size
    y = np.cos(theta)*0+loc
    ax.plot(x,y,z,'r')
    ax.plot(x,-y,z,'r')   

size = 500
loc=0
while(loc<10):
    size -= loc*5
    heart3(size, loc)
    loc+=0.5
    
plt.show()


print(np.linspace(-2 * np.pi, 2 * np.pi, 100))