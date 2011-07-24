"""
n! means n x (n - 1) x ...  3 x 2 x 1

For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

result = str(reduce(lambda a,b: a*b, xrange(10,1,-1)))
print sum([int(x) for x in result])