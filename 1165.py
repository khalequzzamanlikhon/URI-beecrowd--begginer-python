n = int(input())
for i in range(n):
    x = int(input())
    if x==1 or x==2 or x==3:
        print(str(x)+" eh primo")
    else:
        for j in range(2,int(x/2)+1):
            if x%j==0:
                print(str(x) + " nao eh primo")
                break
            else:
                if j!=int(x/2):
                    continue
                else:
                    print(str(x) + " eh primo")