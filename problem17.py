#!/usr/bin/env python

"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342
(three hundred and forty-two) contains 23 letters and 115
(one hundred and fifteen) contains 20 letters. The use of
"and" when writing out numbers is in compliance with British usage.
"""

def main():
	units = ['one', 'two', 'three', 'four', 'five', 'six', 'seven',
			'eight', 'nine']

	tens = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty',
			'seventy', 'eighty', 'ninety']

	elevens = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
			'sixteen', 'seventeen', 'eighteen', 'nineteen']

	# count units
	unitsTotal = 0
	for number in units:
		unitsTotal += len(number)
		print number

	# count tens
	tensTotal = 0
	for number in tens[1:]:
		tensTotal += len(number)
		print number
		for unit in units:
			tensTotal += len(number + unit)
			print number+unit

	# count elevens
	elevensTotal = 0
	elevensTotal += len(tens[0])
	print tens[0]
	for number in elevens:
		elevensTotal += len(number)
		print number

	# count hundreds
	hundredsTotal = 0
	for number in units:
		hundredsTotal += len(number + 'hundred')
		print number+'hundred'

		# units
		for unit in units:
			hundredsTotal += len( number + 'hundredand' + unit )
			print number + 'hundredand' + unit
		# tens
		for ten in tens[1:]:
			hundredsTotal += len( number + 'hundredand' + ten )
			print number + 'hundredand' + ten
			for unit in units:
				hundredsTotal += len ( number + 'hundredand' + ten + unit )
				print number + 'hundredand' + ten + unit
		# elevens
		hundredsTotal += len( number + 'hundredand' + tens[0] )
		print number + 'hundredand' + tens[0]
		for eleven in elevens:
			hundredsTotal += len( number + 'hundredand' + eleven )
			print number + 'hundredand' + eleven

	print sum([unitsTotal, tensTotal, elevensTotal, hundredsTotal, len('onethousand')])

if __name__ == '__main__':
	main()