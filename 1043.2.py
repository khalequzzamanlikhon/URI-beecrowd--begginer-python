a,b,c=input().split()
a=float(a)
b=float(b)
c=float(c)
if a+b>c and b+c>a and c+a>b:
    tri_peri=a+b+c
    print("Perimetro = "+'{:.1f}'.format(tri_peri))
else:
    area=((a+b)*c)/2
    print("Area = "+'{:.1f}'.format(area))