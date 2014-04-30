#!/usr/bin/env python

"""
Find the sum of the digits in the number 100!
"""

from math import factorial
print sum([int(x) for x in str(factorial(100))])