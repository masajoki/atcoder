import math
A,R,N=map(int,input().split())
if N>=31 and R!=1:
    print('large')
    exit()

temp=A*R**(N-1)
if temp>10**9:
    print('large')
else:
    print(temp)
