while 1:
   x,y=input().split()
   x = int(x)
   y = int(y)
   if x<=0 or y<=0:
       break
   elif x<y:
       sum=0
       m=y-x+1
       for i in range(m):
           sum+=x
           print(x,end=' ')
           x+=1
       print("Sum="+str(sum))
   else:
       m=x-y+1
       sum=0
       for i in range(m):
           sum+=y
           print(y,end=' ')
           y+=1
       print("Sum=" + str(sum))