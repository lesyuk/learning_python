def capitalize(word):
    l = list(word)
    for i in range(len(l)):
        if i == 0:
            l[i] = l[i].upper()
        if word[i] == ' ':
            l[i + 1] = l[i + 1].upper()
    print(*l, sep='')


capitalize(input())