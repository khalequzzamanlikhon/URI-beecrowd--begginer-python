x = int(input())
y = int(input())
if x>y:
    sum=0
    for i in range(y,x+1):
        if i%13!=0:
            sum+=i
            #y+=1
else:
    sum=0
    for i in range(x,y+1):
        if i%13!=0:
            sum+=i
print(sum)