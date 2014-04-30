#! /usr/bin/env python

"""
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def main():
	count = 1
	total = 0

	# increment the count to 1000
	while count < 1000:

		# if the count is a multiple of 3 or 5, add it to total
		if count % 3 == 0 or count % 5 == 0:
			total += count

		# increment the count
		count += 1

	# print out the total
	print total

if __name__ == '__main__':
	main()