X,Y=input().split()
X=int(X)
Y=int(Y)
code=[1,2,3,4,5]
price=[4.0,4.5,5.0,2.0,1.5]
for i in range(5):
    if X==code[i]:
        total=Y*price[i]
    else:
        continue
print("Total: R$ "+'{:.2f}'.format(total))
