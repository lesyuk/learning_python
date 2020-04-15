s = input()
fe = s.find('f')

if fe == -1:
    print(-2)
else:
    se = s.find('f', fe + 1)
    if se == -1:
        print(-1)
    else:
        print(se)
