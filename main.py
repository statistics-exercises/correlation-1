import matplotlib.pyplot as plt
import numpy as np

xdata, ydata = 100*[0], 100*[0]
# Your code goes here




# The commands to plot the data 
plt.plot( xdata, ydata, 'bo' )
plt.plot( [0,0], [1,0], 'k-' )
plt.plot( [0,1], [1,1], 'k-' )
plt.plot( [0,1], [0,0], 'k-' )
plt.plot( [1,1], [0,1], 'k-' )
plt.savefig('joint_uniform.png')
