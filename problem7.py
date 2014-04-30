#! /usr/bin/env python

"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10 001st prime number?

Run time of this code has been reduced to less than a second from over 3 minutes
by implementing the algorithm shown in problem 7 overview.
"""

import math

# function to check if a factor is prime
def isPrime(n):
	if n == 1:
		return False
	elif n < 4:
		return True		# 2 and 3 are prime
	elif n % 2 == 0:
		return False
	elif n < 9:
		return True		# we have already excluded 4,6 and 8.
	elif n % 3 == 0:
		return False
	else:
		# root(n) rounded to the greatest integer r so that r*r<=n
		r = math.floor(math.sqrt(n))
		f = 5
		while f <= r:
			if n % f == 0:
				return False
			if n % (f+2) == 0:
				return False
			f += 6

		return True		# in all other cases

def main():
	count = 5
	primes = 3

	# find prime numbers until we find 10001 of them
	while primes < 10001:
		count += 2
		if isPrime(count):
			primes += 1
		
	print count

if __name__ == '__main__':
	main()