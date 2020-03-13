import os
letter = ''
i = 0

with open(os.path.join('/Users/paul/Downloads/dataset_3363_2.txt')) as inf:
    s = inf.readline()
    while i < len(s):
        s[i] * int(s[i + 1])
        i += 2

    # for i in range(len(s)):
    #     if s[i] == s[i + 1 - len(s)]:
    #         letter == s[i]
    #     else:
    #         print(letter * , sep='', end='')