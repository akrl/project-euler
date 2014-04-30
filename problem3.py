#! /usr/bin/env python

"""
What is the largest prime factor of the number 600851475143 ?
"""

def isPrime(factor):
	isFactorPrime = True
	count = 2

	# check if factor divides into any number between 1 and its value
	while count < factor:

		# does the factor divide into count
		if factor % count == 0 and isFactorPrime == True:

			# factor is not prime
			isFactorPrime = False

		# increment count
		count += 1

	return isFactorPrime

def main():
	n = 600851475143
	count = 2
	primeList = []

	while count <= n:

		# check for 2 and 5
		if count == 2 or count == 5:

			if n % count == 0:

				primeList.append(count)

		# check for other numbers
		if str(count)[-1] in ['1', '3', '7', '9']:

			# is count a factor?
			if n % count == 0:

				# is count a prime?
				if isPrime(count) == True:

					# divide number
					n = n / count

					# add count to prime factor list
					primeList.append(count)

		count += 1

	print primeList

if __name__ == '__main__':
	main()