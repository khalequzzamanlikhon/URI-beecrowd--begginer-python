n = float(input())
x=[]
for i in range(100):
    if i==0:
        x.append(n)
    else:
        y=x[i-1]/2
        x.append(y)
for j,k in enumerate(x,start=0):
    print("N"+str([j])+" = {:.4f}".format(k))

