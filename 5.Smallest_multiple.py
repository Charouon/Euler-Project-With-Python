#!/usr/bin/python3

from math import gcd
def lcm(a,b):
    return a*b//gcd(a,b)

from functools import reduce

result = reduce(lcm, range(1,10))
print(result)

#print (lcm(4,10)) ##least common multiple
#print (gcd(12,30)) ##Greatest Common Divisor
