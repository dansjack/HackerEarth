def sum_ab(a, b):
    return int(a) + int(b)


def sum_ab_loop():
    while True:
        try:
            a, b = input().split()
            sum_ab(int(a), int(b))
        except EOFError:
            break


def vowel_recognition(s):
    """
    Returns the number of vowels from every
    possible substring in string s
    :param s: string to analyze
    """
    s = s.lower()
    vowels = 0
    size = len(s)
    for i in range(size):
        if s[i] in 'aeiou':
            #  if el is a vowel, count all the sub strings including el
            #  to the left (i + 1) and right (size - 1) and multiply
            vowels += ((i + 1) * (size - i))

    print(vowels)
    return vowels



def vowel_rec_loop():
    loops = int(input())

    while loops > 0:
        vowel_recognition(input())
        loops -= 1


vowel_recognition('baceb')