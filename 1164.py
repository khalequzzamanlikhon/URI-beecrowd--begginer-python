n= int(input())
for i in range(n):
    sum=0
    x = int(input())
    for j in range(1,x):
        if x%j==0:
            sum+=j
    if sum==x:
        print(str(x)+" eh perfeito")
    else:
        print(str(x)+" nao eh perfeito")
