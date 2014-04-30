#!/usr/bin/env python

"""
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

Construction:
When m and n are any two positive integers (m < n):
	- a = n^2 - m^2
	- b = 2nm
	- c = n^2 + m^2
"""

def main():
	# generates a triplet
	def tripGen(m,n):

		a = n**2 - m**2
		b = 2*n*m
		c = n**2 + m**2

		return (a+b+c,(a,b,c))


	# triplet test
	def tripTest(start):
		n = start
		m = 1

		while m < n and tripGen:
			triplet = tripGen(m,n)

			if triplet[0] <= 1000:

				if triplet[0] == 1000:
					result = (True, triplet)
					break
				else:
					result = False
			else:
				result = False
				break

			m += 1

		return result

	# construct Pythagorean triplets until a + b + c = 1000
	start = 2
	tripletFound = False

	while tripletFound == False:
		triplet = tripTest(start)

		if triplet != False:
			tripletFound = True

			print triplet[1]
			break

		start += 1


if __name__ == '__main__':
	main()