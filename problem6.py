#! /usr/bin/env python

"""
Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""

def main():

	x,y = 0,0

	for n in range(1, 101):
		y += n*n
		x += n

	x *= x

	print x - y

if __name__ == '__main__':
	main()