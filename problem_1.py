"""
Problem 1

If we list all the natural numbers below 10 that are multiples
of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""
# Maneira 1
the_sum = 0
for value in xrange(3,(1000)):
	if value % 3 == 0 or value % 5 == 0:
		the_sum += value
print the_sum

# Maneira 2
print [number for number in xrange(3, 1000) if number % 3 == 0 or number % 5 == 0]