n = int(input())
o = input()
sum=0
for i in range(12):
    for j in range(12):
        x = float(input())
        if j==n:
            sum+=x
if o=="S":
    print("{:.1f}".format(sum))
elif o=="M":
    avg=sum/12
    print("{:.1f}".format(avg))