# Can computers be used to create art?

# Targets:
# Plot a circle, using the parametric equation above.

# Find the parametric equation for Fermat’s Spiral (online), and therefore plot the spiral.

# Do the same for the Butterﬂy Curve.


# Extensions:
# Specify and plot 5 circles with diﬀerent sizes and diﬀerent colours.

# For the Butterﬂy Curve, change the script so that the colour of each line segment changes with the x-coordinate.

# For Fermat’s spiral, plot the curve so that the colour gets lighter with the radius of each line segment.


'''
import matplotlib.pyplot as plt
import numpy as np
import math as m

r = np.arange(0, 8, 0.00001)
#playing around with the step value I realised that decreasing the value resulted in more curved lines
#x = (-1 * r)
#arrange function displays circumference with an r value that varies
theta = (2 * np.pi * (-1 * r))  #
theta_2 = theta + 180
#plots the line as a curving spiral, formulae of circumference of circle

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
fig.set_edgecolor("orange")
ax.plot(theta, r)
ax.plot(theta_2, r)
#ax.plot(theta, x)
#plots circle in radian form, where ax is a function of numpy library and plots the graph
ax.set_rmax(8)
#max value that r can take
array = []
for i in range(0, 8, 1):
  array.append(i)
ax.set_rticks(array)
# Less radial ticks
ax.set_rlabel_position(-22.5)
# Move radial labels away from plotted line
ax.grid(True)
#removes inside grid

ax.set_title("A line plot on a polar axis", va='bottom')
plt.show()
'''
