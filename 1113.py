while 1:
    x,y=input().split()
    x=int(x)
    y=int(y)
    if x==y:
        break
    elif x>y:
        print("Decrescente")
    else:
        print("Crescente")