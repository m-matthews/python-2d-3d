#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Matplotlib Example Program 4: Simple Circle."""

from math import cos, pi, sin
import matplotlib.pyplot as plt


# Data.
segs = 32
x = [sin(pi*2/segs*val) for val in range(0, segs+1)]
y = [cos(pi*2/segs*val) for val in range(0, segs+1)]

# Plot.
plt.plot(x, y)
plt.title("Circle")
plt.axis('off')
plt.show()
