#!/usr/bin/env python

"""
What is the value of the first triangle number to have over five hundred divisors?
"""

"""
Take the 24th triangle number for example. Convert n and n+1 to exponential prime form:
24 = 2^3 * 3^1 * 5^0..., and 25 = 2^0 * 3^0 * 5^2..., respectively.
Then 24*25 = 2^(3+0) * 3^(1+0) * 5^(0+2)..., and thus 24*25/2 = 2^(3-1) * 3^1 * 5^2...
Apply the divisor function (product of exponents plus one) to this last:
(2+1) * (1+1) * (2+1) = 18. Therefore the 24th triangle number has 18 divisors.
Iterate this on n until you find one that produces more than 500. For efficiency,
note that the factors of n+1 will be the factors of n on the subsequent iteration
"""

def primeFactorise(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d += 1
        if d*d > n:
            if n > 1: factors.append(n)
            break

    return factors

def main():
    n = 1

    divisors = 1
    while divisors <= 500:
        divisors = 1

        # convert n to exponential prime form
        nExponential = {}
        primeFactors = primeFactorise(n)
        for prime in primeFactors:
            if prime not in nExponential:
                nExponential[prime] = 1
            else:
                nExponential[prime] += 1

        # convert n+1 to exponential prime form
        primeFactors = primeFactorise(n+1)
        for prime in primeFactors:
            if prime not in nExponential:
                nExponential[prime] = 1
            else:
                nExponential[prime] += 1

        # divide n(n+1) by 2 (subtract 1 from the exponent of prime factor 2)
        nExponential[2] -= 1

        # apply the divisor function to the exponential prime form
        for exponent in nExponential.values():
            divisors *= exponent + 1

        # increment n (next triangular number)
        n += 1


    print "nth triangular number:", n
    print "triangular number:", (n-1)*((n-1)+1)/2
    print "number of divisors:", divisors


if __name__ == '__main__':
    main()