#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Matplotlib Example Program 6: Spiral Animation."""

from math import cos, pi, sin
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter


segs = 180
frames = 75


def update(i):
    plt.clf()
    plt.axis('off')
    # plt.title('Sprial {}/{}'.format(i,frames))
    x = [sin(pi*2/frames*i + pi*2/segs*val) for val in range(0, segs+1)]
    y = [cos(pi*2*3/segs*val) for val in range(0, segs+1)]
    plt.plot(x, y, 'k', linewidth=4.0)


ani = FuncAnimation(plt.figure(), update, range(frames))

writer = PillowWriter(fps=25)
ani.save("06_animation.gif", writer=writer)
plt.show()
