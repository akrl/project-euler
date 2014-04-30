#!/usr/bin/env python

"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

def primes(n):
	if (n <= 2):
		return []

	sieve = [True]*(n+1)
	
	for x in range(3, int(n**0.5)+1, 2):
		for y in range(3, (n//x)+1, 2):
			sieve[(x*y)] = False

	return [2] + [i for i in range(3, n, 2) if sieve[i]]

def main():

	print sum(primes(2000000))

if __name__ == '__main__':
	main()