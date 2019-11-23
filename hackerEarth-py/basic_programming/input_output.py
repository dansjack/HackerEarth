def chars_from_anagram(string1, string2):
    s1 = sorted(string1)
    s2 = sorted(string2)
    length = len(s1) + len(s2)
    matches = 0
    while len(s1) > 0:
        popped = s1.pop()
        if popped in s2:
            matches += 2
            s2.remove(popped)
        print(len(s1))
        print(s1)

    total = length - matches
    print(total)
    return total


def is_palindrome(s):
    """
    Returns YES if s is a palindrome and NO if not
    :param s: String
    :return: YES/NO
    """

    string_list = list(s)
    while len(string_list) > 1:
        if string_list.pop() != string_list.pop(0):
            return 'NO'

    return 'YES'


def find_product(n, int_list):
    """
    :param n: the size of int_list
    :param int_list: a list of integers
    :return: the product of all integers in the list
    """
    answer = 1
    n = int(n)
    for i in int_list:
        answer = (answer * int(i)) % 1000000007
    return answer
