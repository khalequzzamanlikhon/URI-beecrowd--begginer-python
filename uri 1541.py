from math import *
while 1:
    inn=input().split()
    a=int(inn[0])
    if a == 0:
        break
    else:
        b = int(inn[1])
        c = int(inn[2])
        m_area = int(a * b * (100 / c))
        s_area = sqrt(m_area)
        print(int(s_area))





