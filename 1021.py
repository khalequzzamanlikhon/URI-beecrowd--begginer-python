from math import *
n=float(input())
N=n*1000
a=[100,50,20,10,5,2]
b=[1.00,0.50,0.25,0.10,0.05,0.01]
c=[]
d=[]
note=[]
coin=[]
for i in range(6):
    l=a[i]*1000
    c.append(l)

for i in range(6):
    m=b[i]*1000
    d.append(m)
for i in range(6):

    p=floor(N/c[i])
    note.append(p)
    N=N%c[i]
for i in range(6):
    q=floor(N/d[i])
    coin.append(q)
    N=N%d[i]
print("NOTAS:")
for i in range(6):
    print(str(note[i])+" nota(s) de R$ "+str(a[i])+".00")
print("MOEDAS:")
for i  in range(6):
    print(str(coin[i]) + " moeda(s) de R$ "+'{:.2f}'.format(b[i]))