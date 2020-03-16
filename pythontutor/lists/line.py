h = [int(i) for i in input().split()]
x = int(input())
c = 0
for i in range(len(h)):
    if x > h[i]:
        c = i + 1
        print(c)
        break
    elif x == h[i]:
        c = i + 2 # чтобы число встало ЗА значение, а не перед ним
        if i != len(h) - 1:
            if h[i] != h[i + 1 - len(h)]:
                print(c)
                break
            else:
                c += 1
        else:
            print(c)
    else:
        continue
if c == 0:
    print(len(h) + 1)
