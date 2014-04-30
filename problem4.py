#! /usr/bin/env python

"""
Find the largest palindrome made from the product of two 3-digit numbers.
"""

def main():

	x = 999

	largestPalindrome = 0

	while x >= 100:
		y = 999
		while y >= x:

			if x*y <= largestPalindrome:
				break # since x*y is always going to be too small

			n = x * y

			# reverse n and assign it to n2
			n2 = int(str(n)[::-1])

			# palindrome check
			if n == n2:
				largestPalindrome = n

			y -= 1

		x -= 1

	print "Largest palindrome is:"
	print largestPalindrome

if __name__ == '__main__':
	main()