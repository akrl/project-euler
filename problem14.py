#!/usr/bin/env python

"""
Which starting number, under one million, produces the longest Collatz sequence?
"""

def main():
	n = 2
	longestChain = 0

	while n < 1000000:
		currenTerm = n
		totalTerms = 0

		while currenTerm != 1:
			if currenTerm % 2 == 0:
				currenTerm = currenTerm/2
			else:
				currenTerm = 3*currenTerm + 1
			totalTerms += 1

			if totalTerms > longestChain:
				longestChain = totalTerms
				answer = n

		n += 1

	print answer

if __name__ == '__main__':
	main()