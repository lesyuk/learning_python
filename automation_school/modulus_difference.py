a = input()
b = input()
la = list(a)
lb = list(b)
diff_amount = 0
if '-' in la:
    la.remove('-')
if '-' in lb:
    lb.remove('-')

a = ''.join(la)
b = ''.join(lb)

if len(a) != len(b):
    if len(a) > len(b):
        diff = len(a) - len(b)
        b = b.zfill(diff + len(b))
    else:
        diff = len(b) - len(a)
        a = a.zfill(diff + len(a))

for i in range(len(a)):
    diff_amount += abs(int(a[i]) - int(b[i]))

print(diff_amount)
