total = 0
rabit = 0
rat = 0
frog = 0
n = int(input())
for i in range(n):
    a,type=input().split()
    a=int(a)
    total+=a
    if type=='C':
        rabit+=a
    elif type=='R':
        rat+=a
    else:
        frog+=a

frog_percent=(frog/total)*100
rabit_percent=(rabit/total)*100
rat_percent=(rat/total)*100
print("Total: "+str(total)+" cobaias")
print("Total de coelhos: "+str(rabit))
print("Total de ratos: "+str(rat))
print("Total de sapos: "+str(frog))
print("Percentual de coelhos: "+'{:.2f}'.format(rabit_percent)+" %")
print("Percentual de ratos: "+'{:.2f}'.format(rat_percent)+" %")
print("Percentual de sapos: "+'{:.2f}'.format(frog_percent)+" %")




