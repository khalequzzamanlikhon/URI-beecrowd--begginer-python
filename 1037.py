from math import *
a,b,c=input().split()
a=float(a)
b=float(b)
c=float(c)
D=(pow(b,2)-4*a*c)
if D<0 or a==0:
    print("Impossivel calcular")
elif D==0 and a!=0:
    R1 = (-b + sqrt(D)) / (2 * a)
    R2=R1
    print("R1 = " + '{:.5f}'.format(R1))
    print("R2 = " + '{:.5f}'.format(R2))
else:
    R1 = (-b + sqrt(D)) / (2 * a)
    R2 = (-b - sqrt(D)) / (2 * a)
    print("R1 = " + '{:.5f}'.format(R1))
    print("R2 = " + '{:.5f}'.format(R2))


