#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""SVG Example Program 2: Koch Snowflake."""

from math import cos, pi, sin


def line(xs, ys, length, angle, iter):
    """Draw a line with given length and angle, using iter as number of subdivisions to perform."""
    x = xs[-1]
    y = ys[-1]

    if iter < 1:
        xs.append(x+length*sin(angle))
        ys.append(y+length*cos(angle))
    else:
        line(xs, ys, length / 3.0, angle, iter-1)
        line(xs, ys, length / 3.0, angle+pi/3, iter-1)
        line(xs, ys, length / 3.0, angle-pi/3, iter-1)
        line(xs, ys, length / 3.0, angle, iter-1)


def snowflake(pagesize, size, iterations):
    """Generate a Koch Snowflake to fit the given dimensions."""
    # Starting point.
    xs = [pagesize/2 - size/2]
    ys = [pagesize/2 - size/3]
    angle = pi/2

    # Draw the triangle.
    line(xs, ys, size, angle, iterations)
    line(xs, ys, size, angle - pi*2/3, iterations)
    line(xs, ys, size, angle - pi*4/3, iterations)

    return xs, ys


def svg(xs, ys, pagesize, stroke_width=2):
    """Return the SVG representation of this object."""
    points = " ".join([str(x)+" "+str(y) for (x, y) in zip(xs, ys)])

    return '<?xml version="1.0" standalone="no"?>\n' + \
           '<svg width="{0}" height="{0}" version="1.1" xmlns="http://www.w3.org/2000/svg">\n'.format(pagesize) + \
           '  <rect x="0" y="0" width="{0}" height="{0}" fill="white" stroke-width="0"/>\n'.format(pagesize) + \
           '  <polygon points="{}" stroke="forestgreen" fill="transparent" stroke-width="{}"/>\n'.format(points, stroke_width) + \
           '</svg>\n'


pagesize = 500
size = 250

for i in range(6):
    xs, ys = snowflake(pagesize, size, i)

    with open("02_koch_snowflake_{}.svg".format(i), 'w') as f:
        f.write(svg(xs, ys, pagesize))
