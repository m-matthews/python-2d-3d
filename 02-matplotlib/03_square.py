#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Matplotlib Example Program 3: Simple Box."""

import matplotlib.pyplot as plt


# Data.
x = [1, 1, -1, -1, 1]
y = [1, -1, -1, 1, 1]

# Plot.
plt.plot(x, y)
plt.title("Box")
plt.show()

# Plot without axes.
plt.plot(x, y)
plt.title("Box")
plt.axis('off')
plt.show()
