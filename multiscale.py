#!/usr/bin/env python
"""
Copyright (C) 2010 Blair Bonnett, blair.bonnett@gmail.com

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import gettext
_ = gettext.gettext

import inkex
import pathmodifier
import simpletransform

class MultiScaleEffect(inkex.Effect):
    def __init__(self):
        inkex.Effect.__init__(self)
        self.OptionParser.add_option('-s', '--xstart', action='store',
                                     type='float', dest='xstart',
                                     default=1.0, help='Starting scale')
        self.OptionParser.add_option('-f', '--xfinish', action='store',
                                     type='float', dest='xfinish',
                                     default=1.0, help='Finishing scale')
        self.OptionParser.add_option('-x', '--ystart', action='store',
                                     type='float', dest='ystart',
                                     default=1.0, help='Starting scale')
        self.OptionParser.add_option('-z', '--yfinish', action='store',
                                     type='float', dest='yfinish',
                                     default=1.0, help='Finishing scale')

    def effect(self):
        # Check we have enough objects selected
        count = len(self.selected)
        if count < 2:
            inkex.errormsg(_("Please select at least two objects."))

        # The step in scale between each object
        xstep = (self.options.xfinish - self.options.xstart)/(count - 1)
        ystep = (self.options.yfinish - self.options.ystart)/(count - 1)

        # Sort by z order, lowest first
        id_list = self.selected.keys()
        id_list = pathmodifier.zSort(self.document.getroot(), id_list)

        # Scale each object
        xscale = self.options.xstart
        yscale = self.options.ystart
        for id in id_list:
            # No scaling actually happening
            if xscale == 1.0 and yscale == 1.0:
                xscale += xstep
                yscale += ystep
                continue

            # Get node and current transformations
            node = self.selected[id]
            transform = node.get('transform')

            # Scale the object as desired
            if transform:
                transform += ' scale(%f, %f)' % (xscale, yscale)
            else:
                transform = 'scale(%f, %f)' % (xscale, yscale)
            node.set('transform', transform)

            # Change the scale ready for the next object
            xscale += xstep
            yscale += ystep

if __name__ == '__main__':
    e = MultiScaleEffect()
    e.affect()
