a=float(input())
if a >=0 and a <=400.00:
    b = (a*15)/100
    salary = a + b
    p = 15

elif a >= 400.01 and a <= 800.00:
    b = (a*12)/100
    salary = a + b
    p = 12

elif a >= 800.01 and a <= 1200.00:
    b = (a*10)/100
    salary = a + b
    p = 10

elif a >= 1200.01 and a <= 2000.00:
    b = (a*7)/100
    salary = a + b
    p = 7

else:
    b = (a*4)/100
    salary = a + b
    p = 4
print("Novo salario: "+'{:.2f}'.format(salary))
print("Reajuste ganho: "+'{:.2f}'.format(b))
print("Em percentual: "+str(p)+" %")