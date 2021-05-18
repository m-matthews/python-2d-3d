#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Turtle Example Program 2: N-sided Polygon.

Documentation on Turtle: https://docs.python.org/3/library/turtle.html
List of valid colours: https://trinket.io/docs/colors
"""

import turtle


# Initialise.
turtle.shape('turtle')
turtle.color('blue', 'deep sky blue')
turtle.begin_fill()

# Movement of Turtle.
sides = 8
for _ in range(sides):
    turtle.forward(100)
    turtle.left(360/sides)


# Close shape and Fill.
turtle.end_fill()
turtle.done()
