#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Matplotlib Example Program 5: Spiral."""

from math import cos, pi, sin
import matplotlib.pyplot as plt


# Data.
segs = 180
x = [sin(pi*2/segs*val) for val in range(0, segs+1)]
y = [cos(pi*2*3/segs*val) for val in range(0, segs+1)]

# Plot.
plt.plot(x, y, 'k', linewidth=4.0)
# plt.title("Spiral")
plt.axis('off')
plt.show()
