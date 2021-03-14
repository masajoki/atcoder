import math
N=int(input())
a=N//5
i=1
t=0
if N%2==1:
    print(0)
    exit()

while True:
    if N<10:
        print(0)
        exit()
    if 10**i <=N:
        t+=N//(10*i)
        i+=1
    else:
        break
print(t)