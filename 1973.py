n=int(input())
stars=input().split()
stolen=0
sum=0
visited=[]
for i in range(n):
    stars[i]=int(stars[i])
    sum+=stars[i]
    visited.append(0)
i=0
while(1):
   if stars[i]%2==0:
       if i==0:
           visited[i]=1
           if stars[i]>0:
               stars[i]-=1
               stolen+=1
           break
       else:
           visited[i]=1
           if stars[i]>0:
               stars[i]-=1
               stolen+=1
           i-=1
   elif stars[i]%2==1:
       if i==n-1:
           visited[i]=1
           if stars[i]>0:
               stars[i]-=1
               stolen+=1
           break
       else:
           visited[i]=1
           if stars[i]>0:
               stars[i]-=1
               stolen+=1
           i+=1
v_star=0
for x in visited:
    v_star+=x
print(v_star,(sum-stolen))

