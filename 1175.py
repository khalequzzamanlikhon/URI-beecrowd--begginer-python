X = []
for i in range(20):
    x = int(input())
    X.append(x)
j=19
for i in range(10):
    temp=X[i]
    X[i]=X[j]
    X[j]=temp
    j-=1
for k,m in enumerate(X,start=0):
    print("N"+str([k])+" = "+str(m))
