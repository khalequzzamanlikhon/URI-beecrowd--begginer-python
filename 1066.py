even=0
odd=0
positive=0
negative=0
for i in range(5):
    number=int(input())
    if number==0:
        even+=1
    elif number>0:
        positive+=1
        if number%2==0:
            even+=1
        else:
            odd+=1
    else:
        negative += 1
        if number % 2 == 0:
            even += 1
        else:
            odd += 1
print(str(even)+" valor(es) par(es)"+"\n"+str(odd)+" valor(es) impar(es)"+"\n"+str(positive)+" valor(es) positivo(s)"+"\n"+str(negative)+" valor(es) negativo(s)")