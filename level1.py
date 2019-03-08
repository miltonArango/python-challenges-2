"""
Level 1:

The answer to Level 1 is the longest palindrome embedded in the
gettysburg.txt file.

As an example, if the input was "I like racecars that go fast"
the answer would be "racecar".

Test Case:

>>> find_palindrome(''.join('I like racecars that go fast'.split()))
'racecar'
"""
from collections import deque


def find_palindrome(string):
    """Returns the longest palindrome embedded in a string."""

    string_length = len(string)

    # New list to store the palindromes found
    palindromes = []

    # The sliding windows allows to identify palindromes up to the size of the
    # window in this case I use a maximum window size of 100 since it is
    # unlikely for a  palindrome to be this big, unless it is an arbitrary
    # generated palindrome, but for a normal text corpus this works fine.
    for window_size in range(3, 100):
        for n in range(string_length):
            substring = string[n:n + window_size]
            if check_palindrome(substring) and len(substring) > 1:
                palindromes.append(substring)

    return sorted(palindromes, key=len)[-1]


def check_palindrome(string):
    """Checks whether the specified string is a palindrome or not."""
    char_deque = deque()

    for c in string:
        char_deque.appendleft(c)

    equal = True

    while len(char_deque) > 1 and equal:
        first = char_deque.popleft()
        last = char_deque.pop()
        if first != last:
            equal = False
    return equal


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    string = open('gettysburg.txt', 'r')
    print('Longest Palindrome: ' + find_palindrome(string.read()))
    string.close()
