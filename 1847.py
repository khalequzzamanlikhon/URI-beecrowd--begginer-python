a,b,c=list(map(int,input().split()))
diff_ab=a-b
diff_bc=b-c
if diff_ab>0:
    if diff_bc<0 or diff_bc==0:
        print(":)")
    elif diff_bc>0:
        if diff_bc<diff_ab:
            print(":)")
        elif diff_ab==diff_bc:
            print(":(")
        else:
            print(":(")
elif diff_ab<0:
    if diff_bc>0 or diff_bc==0:
        print(":(")
    elif diff_bc<0:
        if abs(diff_bc)<abs(diff_ab):
            print(":(")
        elif diff_ab==diff_bc:
            print(":)")
        elif abs(diff_bc)>abs(diff_ab):
            print(":)")
else:
    if diff_bc<0:
        print(":)")
    else:
        print(":(")

