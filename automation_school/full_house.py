cards = input().split()

d = dict(zip(cards, (0 for i in range(len(cards)))))

for i in cards:
    d[i] += 1

if 3 in d.values() and 2 in d.values():
    print('Full house')
else:
    print('Not full house')
