while 1:
    try:
        n = int(input())
        if n%2==1:
            mid=int(n/2)+1
            p=int (n/3)
            z=[]
            for i in range(n):
                tmp=[]
                for j in range(n):
                    tmp.append(0)
                z.append(tmp)
            for i in range(n):
                for j in range(n):
                   if i>=0 and i<p:
                       if i == j:
                           z[i][j] = 2
                       elif i == n - (j + 1):
                           z[i][j] = 3
                       else:
                           z[i][j]=0
                   elif i>=n-p and i<n:
                       if i == j:
                           z[i][j] = 2
                       elif i == n - (j + 1):
                           z[i][j] = 3
                       else:
                           z[i][j]=0
                   elif i>=p and i<n-p:
                       if j>=0 and j<p:
                           z[i][j]=0
                       elif j >= p and j < n - p:
                           if i == mid - 1 and j == mid - 1:
                               z[i][j] = 4
                           else:
                               z[i][j] = 1
                       else:
                           z[i][j]=0
            for i in range(n):
                for j in range(n):
                    if j!=n-1:
                        print(z[i][j],end='')
                    else:
                        print(z[i][j])
            print("")
    except EOFError:
        break


