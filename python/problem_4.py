"""
Problem 4

A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindrome(number):
	string = str(number)
	if len(string) == 0:
		return True
	return is_palindrome(string[1:-1]) if string[0] == string[-1] else False

lista = []
for x in xrange(10,100):
	for y in xrange(10,100):
		result = x*y
		if is_palindrome(result):
			lista.append(result)
			# print x, 'x', y, ':' ,result
print max(lista)