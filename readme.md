inkscape-multiscale 0.5
=======================

An Inkscape extension to allow multiple objects to be resized with
increasing or decreasing scale factors.

Copyright (C) 2010 Blair Bonnett

Requirements
------------

This extension has only been tested with Inkscape 0.48, but may work
with earlier versions. It is written in Python, so you will need a
version of Inkscape with Python support.

Installation
------------

Copy the multiscale.inx and multiscale.py files to your Inkscape
extensions directory.

Usage
-----

1. Select the objects (at least two objects must be selected) that
   you wish to be resized.
2. Go to Extensions -> Resize -> Multiscale.
3. Set the starting and finishing scales. The starting scale will be
   applied to the lowest object selected, while the finishing scale
   will be applied to the highest. Scale values for the in-between
   objects (in order of their height) will be interpolated from the
   starting and finishing values. For example, if the starting scale
   is 3 and the finishing is 0.5, and you select 6 objects, the scales
   applied will be 3, 2.5, 2, 1.5, 1 and 0.5.

To adjust the height (and therefore the order in which the scales are
applied) of the objects, use the 'Raise', 'Lower', 'Raise to top', or
'Lower to bottom' commands in the 'Object' menu.

Issues
------

SVG scaling works by multiplying the position of each node by the scaling
factor. For example, if you have a line between (100, 100) and (200, 100)
and you scale it by a factor of 1.5, the ends become (150, 150) and
(300, 150). Thus the result appears to be translated as well as scaled.
Future versions of this extension will provide the ability to anchor
either the centre or one edge of each object to remove this apparent
translation.

License
-------

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
