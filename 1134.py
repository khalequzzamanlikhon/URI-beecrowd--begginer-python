alcohol=0
gas=0
diesel=0
while 1:
    x = int(input())
    if x == 1:
        alcohol += 1
    elif x == 2:
        gas += 1
    elif x == 3:
        diesel += 1
    elif x==4:
        print("MUITO OBRIGADO")
        print("Alcool: "+str(alcohol))
        print("Gasolina: " + str(gas))
        print("Diesel: " + str(diesel))
        break
    else:
        continue


