"""
Problem 1

A googol (10**100) is a massive number:
one followed by one-hundred zeros;
100**100 is almost unimaginably large: one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a**b, where a, b < 100, what is the maximum digital sum?
"""

factors = xrange(1,100)
maximum = 0
for x in factors:
	for y in factors:
		result = sum([int(z) for z in str(x**y)])
		if result > maximum:
			maximum = result

print maximum