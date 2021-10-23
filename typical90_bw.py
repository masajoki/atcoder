#075 - Magic For Balls（★3） 
import math
N=int(input())
if N in (2,3,5,7,11):
    print(0)
    exit()

primes={}

for i in range(2,int(N**0.5)+2):
    while N%i==0:
        if i in primes.keys():
            primes[i]+=1
        else:
            primes[i]=1
        N//=i
if N!=1:
    primes[N]=1
    
temp=sum(primes.values())
if temp==0:
    print(0)
else:
    temp2=math.log2(temp)
    print(math.ceil(temp2))