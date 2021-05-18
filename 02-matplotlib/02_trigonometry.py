#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Matplotlib Example Program 2: Trigonometry Functions."""

import math
import matplotlib.pyplot as plt


# Data.
resolution = 90
x = [math.pi*2 / resolution * val for val in range(resolution+1)]
y_sin = [math.sin(val) for val in x]
y_cos = [math.cos(val) for val in x]

# Plot.
plt.plot(x, y_sin)
plt.plot(x, y_cos)
plt.title("Trigonometry Functions")
plt.show()

# Plot.
plt.plot(x, y_sin)
plt.plot(x, y_cos)
plt.title("Trigonometry Functions")
plt.grid(color='lightgray', linestyle='dashed')
plt.xticks([0.0, 1.0, 2.0, 3.0, math.pi, 4.0, 5.0, 6.0, math.pi*2],
           [0, 1, 2, 3, r'$\pi$', 4, 5, 6, r'2$\pi$'])
plt.yticks([-1.0, 0.0, 1.0])
plt.show()

# Plot.
plt.plot(x, y_sin, label='Sine')
plt.plot(x, y_cos, label='Cosine')
plt.legend()
plt.title("Trigonometry Functions")
plt.grid(color='lightgray', linestyle='dashed')
plt.xticks([0.0, 1.0, 2.0, 3.0, math.pi, 4.0, 5.0, 6.0, math.pi*2],
           [0, 1, 2, 3, r'$\pi$', 4, 5, 6, r'2$\pi$'])
plt.yticks([-1.0, 0.0, 1.0])
plt.show()

# Plot.
plt.plot(y_sin, y_cos)
plt.title("Trigonometry Functions")
plt.xticks([-1.0, 0.0, 1.0])
plt.yticks([-1.0, 0.0, 1.0])
plt.show()
