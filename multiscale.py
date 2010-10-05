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
import simpletransform

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
        step = (self.options.startscale - self.options.finishscale)/(count - 1)

        # Apply transform to each node
        scale = self.options.startscale
        for id, node in self.selected.iteritems():
            transform = simpletransform.parseTransform('scale(%f)' % scale)
            simpletransform.applyTransformToNode(transform, node)
            scale += step

if __name__ == '__main__':
    e = MultiScaleEffect()
    e.affect()
