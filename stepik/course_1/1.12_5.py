a, b, c = int(input()), int(input()), int(input())
if a >= b >= c:
    print(a,'\n',c,'\n',b,sep='')
elif a >= c >= b:
    print(a,'\n',b,'\n',c,sep='')
elif b >= a >= c:
    print(b,'\n',c,'\n',a,sep='')
elif b >= c >= a:
    print(b,'\n',a,'\n',c,sep='')
elif c >= a >= b:
    print(c,'\n',b,'\n',a,sep='')
elif c >= b >= a:
    print(c,'\n',a,'\n',b,sep='')
