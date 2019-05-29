# -*- coding: utf-8 -*- 

__author__ = "Road36"
__date__ = "19-5-29"

"""
Describe:
"""

import numpy as np

a = np.empty([3, 2], dtype=str)
print(a)
a[0][0] = "1"
print(a)

