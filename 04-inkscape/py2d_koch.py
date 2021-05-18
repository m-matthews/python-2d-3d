#! /usr/bin/python

from math import pi, sin, cos
import inkex
from py2d import Py2d


class Py2dKoch(Py2d):
    def __init__(self):
        Py2d.__init__(self)

        self.arg_parser.add_argument("--size",
                                     type=float,
                                     dest="size", default=6.0,
                                     help="Size of initial triangle.")
        self.arg_parser.add_argument("--iterations",
                                     type=int,
                                     dest="iterations", default=2.0,
                                     help="Number of iterations.")
        self.arg_parser.add_argument("--linec",
                                     type=str,
                                     dest="linec", default="#000000",
                                     help="Outline color.")
        self.arg_parser.add_argument("--fillc",
                                     type=str,
                                     dest="fillc", default="#00ffff",
                                     help="Fill color.")

    def line(self, length, angle, iter):
        x = self.x[-1]
        y = self.y[-1]

        if iter < 1:
            self.x.append(x+length*sin(angle))
            self.y.append(y+length*cos(angle))
        else:
            self.line(length / 3.0, angle, iter-1)
            self.line(length / 3.0, angle+pi/3, iter-1)
            self.line(length / 3.0, angle-pi/3, iter-1)
            self.line(length / 3.0, angle, iter-1)

    def effect(self):
        Py2d.effect(self)

        size = self.svg.unittouu(str(self.options.size) + self.unit)
        sizex = size
        sizey = size*sin(pi/3)
        iterations = self.options.iterations
        linec = inkex.Color(self.options.linec).to_rgb()
        fillc = inkex.Color(self.options.fillc).to_rgb()

        self.x = [self.docwidth/2 - sizex/2]
        self.y = [self.docheight/2 + sizey/2]
        self.line(size, pi*5/6, iterations)
        self.line(size, pi*1/6, iterations)
        self.line(size, pi*9/6, iterations)

        self.x = self.x[:-1]
        self.y = self.y[:-1]

        self.draw("Koch Snowflake", linec, fillc)


if __name__ == '__main__':
    e = Py2dKoch()
    e.run()
