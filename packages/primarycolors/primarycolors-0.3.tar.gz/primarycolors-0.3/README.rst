=============
primarycolors
=============

Determination of the primary colors in an image file.


Requirements
============
* python (>=2.7.0)
* six
* scipy
* numpy
* Pillow


License:
========

primarycolors is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

primary colors is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with primarycolors.  If not, see http://www.gnu.org/licenses/.

Installation:
=============
::

    $ sudo pip install primarycolors
    
Usage:
======
::

    >>> from primarycolors import PrimaryColors
    >>>
    >>> # `image` - a path to image,
    >>> # `max_colors` - the maximum number of colors in the resulting.
    >>> im = PrimaryColors(image='Lenna.png', max_colors=5)
    >>>
    >>> #  The primary colors in the RGB hexadecimal array
    >>> im.hex_colors
    ['621a43', 'e5bda6', 'd5867b', '9f4257', 'cb6161']
    >>>
    >>> #  The primary colors in the RGB integer array
    >>> im.int_colors
    array([[ 98,  26,  67],
           [229, 189, 166],
           [213, 134, 123],
           [159,  66,  87],
           [203,  97,  97]])
    >>>
    >>> #  An array of primary colors with the frequency coefficients.
    >>> im.sorted_colors
    [('d5867b', 0.2567596435546875),
    ('cb6161', 0.21997451782226562),
    ('621a43', 0.19715118408203125),
    ('9f4257', 0.1964874267578125),
    ('e5bda6', 0.12962722778320312)]


Changelog
=========

0.1 (2015-05-21)
----------------

* First tagged/PyPI'd version.

0.2 (2015-05-21)
----------------

* Fix bugs.

0.3 (2015-01-06)
----------------

* Change API.
* Support Python version 3x.
* Support wheel.
