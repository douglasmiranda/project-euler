"""
It can be seen that the number, 125874, and its double, 251748,
contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x,
and 6x, contain the same digits.
"""

x = 0
while True:
	x += 1
	if not any(n for n in [2,3,4,5,6] if sorted(str(n*x)) != sorted(str(x))):
		break
print x