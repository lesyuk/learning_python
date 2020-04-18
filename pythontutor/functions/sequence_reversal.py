def sequence_reversal():
    n = int(input())
    if n != 0:
        return sequence_reversal(), print(n)
    else:
        return print(0)


sequence_reversal()
