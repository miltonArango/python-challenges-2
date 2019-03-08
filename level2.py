"""
Level 2
----------------------------------------

To determine the answer for Level 2, write code to find the first prime
fibonacci number larger than a given minimum.  For example, the first
prime fibonacci number larger than 10 is 13.

Step 1. Use your code to compute the smallest prime fibonacci number
        greater than 227,000.  Call this number X.

Step 2. The answer for Level 2 is the sum of prime divisors of X + 1.

For the second portion of this task, note that for the number 12 we consider
the sum of the prime divisors to be 2 + 3 = 5.  We do not include 2 twice
even though it divides 12 twice.

Test Case:

>>> solve_level(10)
9
"""


def solve_level(X):
    """ Returns the answer for the step 2 of the Level  """

    # Iterate over the fibonacci numbers using a generator to save
    # memory allocation
    for num in fibonacci():
        # Check if the number is greater than the minimum and also if
        # it is prime (i.e. Only has 1 prime factor)
        if num > X and len(factor(num)) == 1:
            factors = factor(num + 1)
            return sum(set(factors))


def fibonacci():
    """ Generator yielding Fibonacci numbers"""
    x, y = 0, 1
    while True:
        yield x
        x, y = y, x + y


def factor(number):
    """ Checks if the given number is prime using Trial division
        :returns list containing the prime factors
    """
    factors = []
    f = 2

    while number > 1:
        if number % f == 0:
            factors.append(f)
            number /= f
        else:
            f += 1
    return factors


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print('Level2 Answer: %d' % solve_level(277000))
