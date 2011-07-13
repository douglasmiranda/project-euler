"""
2520 is the smallest number that can be divided by
each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly
divisible by all of the numbers from 1 to 20?
"""
x = 0

while True:
	verify = True
	x += 1
	for y in xrange(1, 21):
		if not x % y == 0:
			verify = False
			break

	if verify:
		break

print x