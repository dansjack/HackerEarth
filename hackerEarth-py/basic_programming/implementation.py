def count_digits(s):
    """
    You are given a string S. Count the number of occurrences of all
    the digits in the string S.

    Input:
    First line contains string S.

    Output:
    For each digit starting from 0 to 9, print the count of their
    occurrences in the string S. So, print
    lines, each line containing 2 space separated integers.
    First integer i and second integer count of occurrence of i.
    """
    digits = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0,
              '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
    for i in s:
        digits[i] += 1
    for el in sorted(digits.items()):
        print('{} {}'.format(el[0], el[1]))


