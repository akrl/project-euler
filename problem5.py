#! /usr/bin/env python

"""
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def main():

	count = 20
	answer = 0
	realAnswer = 0

	debug = 10000

	while answer < 20:

		#print "answer is less than 20. answer is: " + str(answer)

		answer = 0
		divider = 3
		#print "divider is 1"

		while divider <= 20:

			#print "divider is less than 20. divider is: " + str(divider)

			if count % divider == 0:

				#print "count divides into divider. count is: " + str(count) + " divider is " + str(divider)

				answer += 1

				#print "answer is incremented by 1. answer is: " + str(answer)

			if answer == 20:

				#print "answer is 20. realAnswer is set to count. count is: " + str(count)

				realAnswer = count

			divider += 2
			#print "divider is incremented. divider is: " + str(divider)

		if count == debug:
			print count
			debug += 1000000

		count +=1
		#print "count is incremented. count is: " + str(count)

	print realAnswer

if __name__ == '__main__':
	main()