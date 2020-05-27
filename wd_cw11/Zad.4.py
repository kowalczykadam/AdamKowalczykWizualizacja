import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# konfiguracja wielkości wykresu, figsize określa wielkość wykresu w calach
fig = plt.figure( figsize =( 8 , 3 ))
ax1 = fig.add_subplot( 231 , projection = '3d' )
ax2 = fig.add_subplot( 232 , projection = '3d' )
ax3 = fig.add_subplot( 233 , projection = '3d' )
ax4 = fig.add_subplot( 234 , projection = '3d' )
ax5 = fig.add_subplot( 236 , projection = '3d' )
# fikcyjne dane
_x = np.arange( 4 )
_y = np.arange( 5 )
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()
top = x + y
bottom = np.zeros_like(top)
width = depth = 1
ax1.bar3d(x, y, bottom, width, depth, top, shade = True )
ax1.set_title('Wykres zacieniony')
ax2.bar3d(x, y, bottom, width, depth, top, shade = False )
ax2.set_title('Wykres nie zacieniony')
ax3.bar3d(x, y, bottom, width, depth, top, shade = False, color = 'g' )
ax3.set_title('Wykres nie zacieniony zielony')
ax4.bar3d(x, y, bottom, width, depth, top, shade = True, color = 'g' )
ax4.set_title('Wykres zacieniony zielony')
ax5.bar3d(x, y, bottom, width, depth, top, shade = True, color = 'r' )
ax5.set_title('Wykres zacieniony czerwony')
plt.show()