"""
Level 3
----------------------------------------

For the final level, you must find all subsets of an array where the
largest number is the sum of the remaining numbers.
For example, for an input of:

(1, 2, 3, 4, 6)

the subsets would be

1 + 2 = 3
1 + 3 = 4
2 + 4 = 6
1 + 2 + 3 = 6

The numbers.csv file contains the list of numbers you should run your code
on. The password is the number of subsets.  In the above case the answer
would be 4.

Test Case:

>>> find_subsets([1, 2, 3, 4, 6])
4
"""


def find_subsets(array):
    pass


def is_subset_sum(subset, s):
    c_sum = 0
    sub = []
    for n in subset:
        c_sum += n
        if c_sum == s:
            sub.append(n)


if __name__ == "__main__":
    # import doctest
    # doctest.testmod()
    file = open('numbers.csv', 'r')
    array = [int(x) for x in file.read().split(',')]
    # print('Password: %d' % find_subsets(array.read()))
    find_subsets([1, 2, 3, 4, 6])
    file.close()
