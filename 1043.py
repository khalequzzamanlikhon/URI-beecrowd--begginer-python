a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
if a>b and a>c:
    max=a
    if b>c:
        mid=b
        min=c
    else:
        mid=c
        min=b
elif b>a and b>c:
    max=b
    if(a>c):
        mid=a
        min=c
    else:
        mid=c
        min=a
else:
    max=c
    if(a>b):
        mid=a
        min=b
    else:
        mid=b
        min=a

print(str(min)+"\n"+str(mid)+"\n"+str(max)+"\n")

print(str(a)+"\n"+str(b)+"\n"+str(c))