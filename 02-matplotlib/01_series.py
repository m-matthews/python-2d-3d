#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Matplotlib Example Program 1: Plotting Data Series."""

import matplotlib.pyplot as plt


# Fixed Data.
xvals = [1, 2, 3, 4, 5]
yvals = [1, 2, 1, 2, 1]

plt.plot(xvals, yvals)
plt.title("Series 1")
plt.show()

# Series Data using Range().
xvals = [val for val in range(10)]
yvals = [x*2 for x in xvals]
plt.plot(xvals, yvals, 'bo-')
plt.title("Series 2")
plt.xlabel("* Note that range(10) returns values from 0 to 9.")
plt.show()
