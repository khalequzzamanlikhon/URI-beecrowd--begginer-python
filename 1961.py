p,n=map(int,input().split())
pipes=input().split()
for j in range(n):
    pipes[j]=int(pipes[j])
flag=0
for i in range(n-1):
    if abs(pipes[i] -pipes[i + 1]) > p:
        flag = 0
        print("GAME OVER")
        break
    else:
        flag = 1
if flag == 1:
     print("YOU WIN")
