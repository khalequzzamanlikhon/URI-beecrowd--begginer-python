while 1:
    n = int(input())
    if n==0:
        break
    else:
        z=[]
        x=0
        y=n
        for i in range(x,y):
            temp=[]
            for j in range(x,y):
                temp.append(1)
            z.append(temp)
        for i in range(n):
            p=i+1
            s=2
            for j in range(n):
                if j<=i:
                    z[i][j]=p
                    p-=1
                else:
                    q=i+1
                    z[i][j]=s
                    s+=1
        for i in range(n):
            t=""
            for j in range(n):
                t+=" %3d"%z[i][j]
            print(t[1:])
        print("")