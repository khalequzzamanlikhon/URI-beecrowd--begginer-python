input=float(input())
if input<0 or input>100:
    print("Fora de intervalo")
else:
     if input>=0 and input<=25:
        print("Intervalo [0,25]")
     elif input>25 and input<=50:
         print("Intervalo (25,50]")
     elif input > 50 and input <= 75:
        print("Intervalo (50,75]")
     else:
        print("Intervalo (75,100]")