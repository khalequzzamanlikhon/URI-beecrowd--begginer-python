from math import *
input=int(input())
hours=floor(input/3600)
input=input%3600
minutes=floor(input/60)
seconds=input%60
print(str(hours)+":"+str(minutes)+":"+str(seconds))