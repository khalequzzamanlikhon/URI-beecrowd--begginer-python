n=int(input())
for i in range(n):
    inn=int(input())
    if inn<2015:
        result=2015-inn
        print(result,'D.C.')
    else:
        result=inn-2014
        print(result,'A.C.')
