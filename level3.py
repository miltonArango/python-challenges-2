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
    """ Returns all the subsets of an array where an element in the array
        can be expressed as the sum of the subset. The array must be sorted
        in ascending order for the algorithm to work correctly.
    """
    subsets = []
    for number in reversed(array):
        index = array.index(number)
        for i in range(index - 1):
            subset = subset_sum(array[i:index], number)
            if subset:
                subsets.append(subset)
    return len(subsets)


def subset_sum(subset, number):
    """ Checks recursively if the sum of the elements in the subset adds
        to the number. If not, returns False, otherwise returns the subset
        that is equivalent to the number.
     """

    # Base cases:
    if number < 1:
        return False
    elif len(subset) == 0:
        return False
    if subset[0] == number:
        return [subset[0]]
    else:
        # Recursive step:
        # If the first element of the array is not equal to the number
        # do a recursion step excluding the first element and substract
        # the first element from the number.
        recursive_sum = subset_sum(subset[1:], (number - subset[0]))

        # If the recursive sum returns a subset appends it to the first
        # element.
        if recursive_sum:
            return [subset[0]] + recursive_sum
        # Otherwise is not possible to get the sum of the number using
        # the first element, so we repeat the recursion excluding it.
        else:
            return subset_sum(subset[1:], number)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    file = open('numbers.csv', 'r')
    array = [int(x) for x in file.read().split(',')]
    print('Password: %d' % find_subsets(array))
    file.close()
