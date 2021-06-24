import math
N=int(input())
temp=math.floor(N*1.08)
if temp<206:
    print("Yay!")
elif temp==206:
    print("so-so")
elif temp>206:
    print(":(")
