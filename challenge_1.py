# Can computers be used to create art?

import numpy as np
import matplotlib.pyplot as plt
import random as r


k = 5
a = np.linspace(k, k, 10 ** 6)
phi = np.linspace(0, 12 * np.pi, 10 ** 6)
t = np.linspace(0, 24 * np.pi, 10 ** 4)


# Targets:

# Plot a circle, using the parametric equation above.
x = k * np.cos(t)
y = k * np.sin(t)
plt.plot(x, y)
plt.show()

# Find the parametric equation for Fermat’s Spiral (online), and therefore plot the spiral.
x = k * np.sqrt(t) * np.cos(t)
y = k * np.sqrt(t) * np.sin(t)
u = -k * np.sqrt(t) * np.cos(t)
v = -k * np.sqrt(t) * np.sin(t)
plt.plot(x, y)
plt.plot(u, v)
plt.show()

# Do the same for the Butterﬂy Curve.
x = np.sin(t) * ((np.e ** np.cos(t)) - (2 * np.cos(4 * t)) - (np.sin(t / 12) ** 5))
y = np.cos(t) * ((np.e ** np.cos(t)) - (2 * np.cos(4 * t)) - (np.sin(t / 12) ** 5))
plt.plot(x, y)
plt.show()


# Extensions:

# Specify and plot 5 circles with different sizes and different colours.
ran = r.randint(1, 100)
x1 = ran * np.cos(t)
y1 = ran * np.sin(t)
plt.plot(x1, y1)

ran = r.randint(1, 100)
x2 = ran * np.cos(t)
y2 = ran * np.sin(t)
plt.plot(x2, y2)

ran = r.randint(1, 100)
x3 = ran * np.cos(t)
y3 = ran * np.sin(t)
plt.plot(x3, y3)

ran = r.randint(1, 100)
x4 = ran * np.cos(t)
y4 = ran * np.sin(t)
plt.plot(x4, y4)

ran = r.randint(1, 100)
x5 = ran * np.cos(t)
y5 = ran * np.sin(t)
plt.plot(x5, y5)

plt.show()

# For the Butterﬂy Curve, change the script so that the colour of each line segment changes with the x-coordinate.
'''
https://matplotlib.org/stable/tutorials/colors/colors.html#sphx-glr-tutorials-colors-colors-py
'''

# For Fermat’s spiral, plot the curve so that the colour gets lighter with the radius of each line segment.
