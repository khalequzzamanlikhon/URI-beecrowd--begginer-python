count=0
sum=0
x = int(input())
while 1:
    y= int(input())
    if y>x:
        break
    else:
        continue

if x<y:
    while 1:
        sum+=x
        count += 1
        x+=1
        if sum>y:
            print(count)
            break


