p_c=0
ip_c=0
par = []
im_par = []
for i in range(15):
    x = int(input())
    if x%2==0:
        par.insert(p_c,x)
        p_c+=1
        if p_c==5:
            for j,k in enumerate(par,start=0):
                print("par"+str([j])+" = "+str(k))
                p_c=0
    else:
        im_par.insert(ip_c,x)
        ip_c += 1
        if ip_c==5:
            for l,m in enumerate(im_par,start=0):
                print("impar"+str([l])+" = "+str(m))
                ip_c=0

for i in range(ip_c):
    print("impar" + str([i]) + " = " + str(im_par[i]))
for i in range(p_c):
    print("par" + str([i]) + " = " + str(par[i]))