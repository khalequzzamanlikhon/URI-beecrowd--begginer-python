n= int(input())
flag=0
for i in range(n):
    option=input().split()
    sheldon,raj=list(map( str,option))
    if sheldon==raj:
           flag=2
    if sheldon=="tesoura" and raj=="papel":
        flag=0
    elif sheldon=="papel" and raj=="tesoura":
       flag=1
    if sheldon=="papel" and raj=="pedra":
       flag=0
    elif sheldon=="pedra" and raj=="papel":
      flag=1
    if sheldon=="pedra" and raj=="lagarto":
       flag=0
    elif  sheldon=="lagarto" and raj=="pedra":
       flag=1
    if sheldon=="lagarto" and raj=="Spock":
      flag=0
    elif  sheldon=="Spock" and raj=="lagarto":
       flag=1
    if sheldon=="Spock" and raj=="tesoura":
       flag=0
    elif  sheldon=="tesoura" and raj=="Spock":
       flag=1
    if sheldon=="tesoura" and raj=="lagarto":
        flag=0
    elif  sheldon=="lagarto" and raj=="tesoura":
      flag=1
    if sheldon=="lagarto" and raj=="papel":
       flag=0
    elif  sheldon=="papel" and raj=="lagarto":
        flag=1
    if sheldon=="papel" and raj=="Spock":
       flag=0
    elif  sheldon=="Spock" and raj=="papel":
      flag=1
    if sheldon=="Spock" and raj=="pedra":
        flag=0
    elif  sheldon=="pedra" and raj=="Spock":
      flag=1
    if sheldon=="pedra" and raj=="tesoura":
      flag=0
    elif  sheldon=="tesoura" and raj=="pedra":
      flag=1
    if flag==2:
        print('Caso #{}: De novo!'.format(i+1))
    elif flag==0:
        print('Caso #{}: Bazinga!'.format(i+1))
    elif flag==1:
        print('Caso #{}: Raj trapaceou!'.format(i+1))
