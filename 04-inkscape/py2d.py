#! /usr/bin/python

import gettext
import inkex
from lxml import etree


class Py2d(inkex.Effect):
    def __init__(self):
        inkex.Effect.__init__(self)

        self.arg_parser.add_argument("--active-tab",
                                     type=str,
                                     dest="tab", default="Options",
                                     help="The tab selected when OK was pressed")
        self.arg_parser.add_argument("--unit",
                                     type=str,
                                     dest="unit", default="mm",
                                     help="unit of measure for circular pitch and center diameter")
        self.arg_parser.add_argument("--linethickness",
                                     type=str,
                                     dest="linethickness", default="1px",
                                     help="Line Thickness")

    def effect(self):
        self.unit = self.options.unit
        self.linethickness = self.svg.unittouu(self.options.linethickness)

        self.docwidth = self.svg.unittouu(self.svg.get('width'))
        self.docheight = self.svg.unittouu(self.svg.get('height'))

        self.parent = self.svg.get_current_layer()

        layer = etree.SubElement(self.svg, 'g')
        layer.set(inkex.addNS('label', 'inkscape'), 'newlayer')
        layer.set(inkex.addNS('groupmode', 'inkscape'), 'layer')

        self.x = []
        self.y = []

    def generate_svg(self):
        # Generate SVG string for this trace.
        if len(self.x) < 2:
            return ""
        return "M {} {} ".format(self.x[0], self.y[0]) + \
               " ".join(["L {} {}".format(x, y) for x, y in zip(self.x[1:], self.y[1:])]) + " z"

    def draw(self, label, linec, fillc):
        line_style = {'stroke': linec,
                      'stroke-width': str(self.linethickness),
                      'fill': fillc}

        line_attribs = {'style': str(inkex.Style(line_style)),
                        inkex.addNS('label', 'inkscape'): label,
                        'd': self.generate_svg()}

        _ = etree.SubElement(self.parent, inkex.addNS('path', 'svg'), line_attribs)

    def _debug(self, string):
        inkex.debug(gettext.gettext(str(string)))

    def _error(self, string):
        inkex.errormsg(gettext.gettext(str(string)))
