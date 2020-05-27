import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.axes3d import get_test_data
from mpl_toolkits.mplot3d import Axes3D

np.random.seed( 19680801 )


def randrange(n, vmin, vmax):
    
    return (vmax - vmin)*np.random.rand(n) + vmin


fig = plt.figure( figsize =plt.figaspect( 0.5 ))
#===============
# Pierwszy wykres
#===============
# osie dla pierwszego wykresu
ax = fig.add_subplot( 1 , 2 , 1 , projection = '3d' )
n = 20
for c, m, zlow, zhigh in [( 'r' , 'o' , - 50 , - 25 )]:
    xs = randrange(n, 23 , 32 )
    ys = randrange(n, 0 , 100 )
    zs = randrange(n, zlow, zhigh)
    ax.scatter(xs, ys, zs, c =c, marker =m)
#===============
# Drugi wykres
#===============
# Osie dla drugiego wykresu
ax = fig.add_subplot( 1 , 2 , 2 , projection = '3d' )
t = np.linspace( 0 , 2 * np.pi, 5 )
z = t
x = np.sin(t)
y = np.cos(t)
ax.plot(x, y, z)