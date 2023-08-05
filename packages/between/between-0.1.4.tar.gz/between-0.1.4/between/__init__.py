# -*- coding: UTF-8 -*-

"""
between for Python
~~~~~~~~~~~~~~~~~~

Between of VCNC for Python. Basic usage:

    >>> import between
    >>> client = betweeen.Client("YOUR_ID", "YOUR_PASSWORD")
    >>> client.sendMessage("Carpe diem!")

:copyright: (c) 2015 by Taehoon Kim.
:license: BSD, see LICENSE for more details.
"""


from .client import *


__copyright__ = 'Copyright 2015 by Taehoon Kim'
__version__ = '0.1.4'
__license__ = 'BSD'
__author__ = 'Taehoon Kim'
__email__ = 'carpedm20@gmail.com'
__source__ = 'https://github.com/carpedm20/between/'

__all__ = [
    'Client',
]
