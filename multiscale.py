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

class MultiScaleEffect(inkex.Effect):
    def __init__(self):
        inkex.Effect.__init__(self)
        self.OptionParser.add_option('-s', '--startscale', action='store',
                                     type='float', dest='startscale',
                                     default=1.0, help='Starting scale')
        self.OptionParser.add_option('-f', '--finishscale', action='store',
                                     type='float', dest='finishscale',
                                     default=1.0, help='Finishing scale')

    def effect(self):
        # Check we have enough objects selected
        count = len(self.selected)
        if count < 2:
            inkex.errormsg(_("Please select at least two objects."))

        # The step in scale between each object
        step = (self.options.finishscale - self.options.startscale)/(count - 1)

        # Sort by z order, lowest first
        id_list = self.selected.keys()
        id_list = pathmodifier.zSort(self.document.getroot(), id_list)

        # Scale each object
        scale = self.options.startscale
        for id in id_list:
            # Get node and current transformations
            node = self.selected[id]
            transform = node.get('transform')

            # Scale the object as desired
            if transform:
                transform += ' scale(%f)' % scale
            else:
                transform = 'scale(%f)' % scale
            node.set('transform', transform)

            # Change the scale ready for the next object
            scale += step

if __name__ == '__main__':
    e = MultiScaleEffect()
    e.affect()
