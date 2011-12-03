# The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

# (Please note that the palindromic number, in either base, may not include leading zeros.)

def is_palindrome(word):
	if len(word) == 0:
		return True
	return is_palindrome(word[1:-1]) if word[0] == word[-1] else False

sum_of_all = 0
for number in xrange(0, 1000000):
	binary = bin(number)
	# was the easyst way that i found to solve the leading zeros " str(binary)+'b0' "
	if is_palindrome(str(binary)+'b0') and is_palindrome(str(number)):
		sum_of_all += number

print sum_of_all