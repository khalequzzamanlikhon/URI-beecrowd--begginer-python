
a=int(input())
b=int(input())
sum=0
if a>b:
    max=a
    min=b
else:
    max=b
    min=a
for i in range((min+1),max):
    if i%2==1 or i%2==-1:
        sum+=i
print(sum)