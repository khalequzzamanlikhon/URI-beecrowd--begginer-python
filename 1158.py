n = int(input())
for l in range(n):
    sum=0
    x, y = input().split()
    x = int(x)
    y = int(y)
    if x%2==0:
        x+=1
    for i in range(y):
        sum+=x
        x+=2
    print(sum)


