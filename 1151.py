n = int(input())
first=0
second=1
print(first,end=' ')
print(second,end=' ')
for i in range(2,n):
    new=first+second
    first=second
    second=new
    if i!=n-1:
        print(new,end=' ')
    else:
        print(new)