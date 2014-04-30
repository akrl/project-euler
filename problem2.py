#! /usr/bin/env python

"""
By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.
"""

def main():

	total = 2

	currentTerms = [1,2]

	# find next term, as long as it is less than 4 mil
	# check if new term is even, if so, add it to total

	while currentTerms[1] < 4000000:

		# find next term
		nextTerm = currentTerms[0] + currentTerms[1]

		# check if new term is even
		if nextTerm % 2 == 0:

			# add the new term to total
			total += nextTerm

		# update currentTerms
		currentTerms = [currentTerms[1], nextTerm]


	# print total
	print total

if __name__ == '__main__':
	main()