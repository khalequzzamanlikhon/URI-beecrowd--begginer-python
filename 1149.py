sum=0
a=list(map(int,input().split()))
while 1:
    x,y = input().split()
    x=int(x)
    y=int(y)
    while 1:
        y = int(y)
        if y>0:
            break
        else:
            continue

    for i in range(y):
        sum+=x
        x+=1
    print(sum)
    break

