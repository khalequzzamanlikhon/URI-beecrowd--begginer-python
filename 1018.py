from math import *
a=[100,50,20,10,5,2,1]
b=[]
N=int(input())
print(N)
for i in range(7):
    b1=floor(N/a[i])
    N=N%a[i]
    b.append(b1)

for i in range(7):
    print(str(b[i])+" nota(s) de R$ "+str(a[i])+",00")

