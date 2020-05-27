# Projekcja 3d
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

np.random.seed( 19680800 )


def randrange(n, vmin, vmax):
    
    return (vmax - vmin)*np.random.rand(n) + vmin


fig = plt.figure()
ax = fig.gca( projection = '3d' )
n = 20
for c, m, zlow, zhigh in [( 'r' , 'o' , - 50 , - 25 )]:
    xs = randrange(n, 0 , 10 )
    ys = randrange(n, 0 , 10 )
    ax.scatter(xs, ys, zs = 0, zdir = 'x', c =c, marker =m)

t = np.linspace( 0 , 2 * np.pi, 5 )
ys = t
xs = abs(np.cos(t))
ax.plot(xs, ys, zs = 0, zdir = 'x', color='g')
# Limity dla legendy
ax.legend()
ax.set_xlim( 0 , 10 )
ax.set_ylim( 0 , 10 )
ax.set_zlim( 0 , 10 )
ax.set_xlabel( 'X' )
ax.set_ylabel( 'Y' )
ax.set_zlabel( 'Z' )
# Ustawienie kąta nachylenia przy generowaniu wykresu
# oś y=0
ax.view_init( elev = 20. , azim =- 35 )
plt.show()