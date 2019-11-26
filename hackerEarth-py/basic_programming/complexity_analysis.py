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
    i = 0
    s2 = ''
    while True:
        if size < 1:  # Reached front of list
            size = len(s)
            if i > size:  # Checked all substrings, exit loop
                break
            i += 1
        s2 += s[i:size]
        size -= 1

    for i in 'aeiou':
        vowels += s2.count(i)

    print(vowels)
    return vowels



def vowel_rec_loop():
    loops = int(input())

    while loops > 0:
        vowel_recognition(input())
        loops -= 1


vowel_recognition('baceb')