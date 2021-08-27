import math
t,N=map(int,input().split())
for i in range(N):
    print(i,math.floor(i*(100+t)/100))
