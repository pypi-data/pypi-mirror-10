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
    >>> im.hex
    ['621b43', '9e4257', 'e5bca5', 'd6877b', 'cb6161']
    >>> im.web
    ['#621b43', '#9e4257', '#e5bca5', '#d6877b', '#cb6161']

    >>> #  The primary colors in the RGB integer array
    >>> im.rgb
    [[ 98,  27,  67], [158,  66,  87], [229, 188, 165], [214, 135, 123], [203,  97,  97]]
    >>>
    >>> #  An array of primary colors with the frequency coefficients.
    >>> im.sorted_colors
    [('cb6161', 0.24160000000000001),
     ('d6877b', 0.2412),
     ('621b43', 0.2016),
     ('9e4257', 0.1908),
     ('e5bca5', 0.12479999999999999)]
    >>> im.hsl
    [(326, 56.799999999999997, 24.509803921568629),
     (346, 41.071428571428569, 43.921568627450981),
     (21, 55.172413793103459, 77.254901960784323),
     (7, 52.601156069364166, 66.078431372549019),
     (0, 50.47619047619046, 58.823529411764696)]



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

0.4 (2015-02-06)
----------------

* Change API.
* Increased performance.
* Added the methods `web` and `hsl`.
