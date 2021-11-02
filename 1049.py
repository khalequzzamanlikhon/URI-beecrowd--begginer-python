a="vertebrado"
a1="ave"
a2="mamifero"
a11="carnivoro"
a12="onivoro"
a22="herbivoro"
m1="aguia"
m2="pomba"
m3="homen"
m4="vaca"
b="invertebrado"
b1="inseto"
b2="anelideo"
b11="hematofago"
m5="pulga"
m6="lagarta"
m7="sanguessuga"
m8="minhoca"
d=input()
if d==a:
    e=input()
    if e==a1:
        f=input()
        if f==a11:
            print("aguia")
        elif f==a12:
            print("pomba")
    if e==a2:
        f=input()
        if f==a12:
            print("homen")
        elif e==a22:
            print("vaca")
elif d==b:
    e=input()
    if e==b1:
        f=input()
        if f==b11:
            print("pulga")
        elif f==a22:
            print("lagarta")
    if e==b2:
        f=input()
        if f==b11:
            print("sanguessuga")
        elif f==a12:
            print("minhoca")

