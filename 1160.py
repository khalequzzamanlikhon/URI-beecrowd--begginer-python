n = int(input())
for i in range(n):
    p1, p2, g1, g2 = input().split()
    p1 = int(p1)
    p2 = int(p2)
    g1 = float(g1)
    g2 = float(g2)
    time = 0
    while 1:
        if p1>p2:
            if time<=100:
                print(str(time),"anos.")
                break
        elif p1<=p2:
            p1 = int(p1*(1 + g1/100))
            p2=int(p2*(1+g2/100))
            time += 1
            if time>100:
                print("Mais de 1 seculo.")
                break





