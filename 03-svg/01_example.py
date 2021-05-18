#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""SVG Example Program 1: Example."""

from math import cos, pi, sin


with open("01_example.svg", "w") as f:
    f.write('<?xml version="1.0" standalone="no"?>\n')
    f.write('<svg width="250" height="250" version="1.1" xmlns="http://www.w3.org/2000/svg">\n')

    f.write('  <rect x="2" y="2" width="246" height="246" stroke="blue" fill="white" stroke-width="5"/>\n')

    x = [125.0 + sin(val*pi/180)*90.0 + sin(val*16*pi/180)*20.0 for val in range(360)]
    y = [125.0 + cos(val*pi/180)*90.0 + cos(val*16*pi/180)*20.0 for val in range(360)]
    vals = " ".join([str(x1)+' '+str(y1) for (x1, y1) in zip(x, y)])
    f.write('  <polygon points="{}" stroke="forestgreen" fill="transparent" stroke-width="2"/>\n'.format(vals))

    f.write('  <circle cx="125" cy="125" r="50" stroke="limegreen" fill="transparent" stroke-width="2"/>\n')

    f.write('  <line x1="85" x2="165" y1="85" y2="165" stroke="orangered" stroke-width="2"/>\n')

    f.write('</svg>\n')
