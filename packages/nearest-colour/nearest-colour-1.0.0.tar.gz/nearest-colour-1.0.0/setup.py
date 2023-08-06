# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nearest_colours']

package_data = \
{'': ['*']}

install_requires = \
['colour>=0.1.5,<0.2.0', 'numpy>=1.22.0,<2.0.0', 'pandas>=1.3.5,<2.0.0']

setup_kwargs = {
    'name': 'nearest-colour',
    'version': '1.0.0',
    'description': 'Find the nearest W3C/X11 named colors to a given color',
    'long_description': '# Nearest Colours\n\n[![](https://img.shields.io/badge/version-1.0.0-green)](https://pypi.org/project/nearest-colour)\n![](https://img.shields.io/badge/Python-&ge;3.8-blue)\n\nFind the nearest W3C/X11 named colors to a given color.\nThis module, `nearest_colour`, provides two functions:\n\n```python\nfrom typing import List, Literal, Union\nfrom colour import Color\n\nColorSpace = Literal["hsv", "rgb", "yiq", "hls"]\n\ndef nearest_x11(color: Union[Color, str], n: int = 1, space: ColorSpace = "hls") -> List[Color]:\n    pass\n\n\ndef nearest_w3c(color: Union[Color, str], n: int = 1, space: ColorSpace = "hls") -> List[Color]:\n    pass\n```\n\nEach will return the `n` colors that are closest (Euclidean distance) to `color` in the specified color-`space` from either the set of W3C web colors or the set of Unix X11 colors.\nWeb colors are [standardized by W3C][W3C colors], whereas Unix X11 colors are [defined in the X11 source-code][X11 colors].\n**Note:** these two sets of colors are almost entirely overlapping, but not completely.\nColors may be provided as either [colour] `Color` objects, or as W3C colors strings.\nThe default color-space for distance computation is HSL, which is perceptually uniform and therefore returns colors which are perceptually closer to the given color.\nA list is always returned, even if `n == 1`, and the ordering is from most similar to least similar.\nIf you pass a large wnough integer (say, 256), you\'ll get the ranking for all colors in the respective set.\n\n[colour]: https://pypi.org/project/colour/\n[X11 colors]: https://gitlab.freedesktop.org/xorg/xserver/blob/master/os/oscolor.c\n[W3C colors]: https://www.w3.org/wiki/CSS/Properties/color/keywords\n',
    'author': 'Pedro Asad',
    'author_email': 'psa.exe@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/pedroasad/python-nearest-colour',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
