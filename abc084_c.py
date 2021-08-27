N=int(input())
import math
C,S,F=[],[],[]
for i in range(N-1):
    c,s,f=map(int,input().split())
    C.append(c)
    S.append(s)
    F.append(f)

def calc(s):
    temp=S[s]+C[s]
    for i in range(s+1,N-1):
        if temp<=S[i]:
            temp=S[i]+C[i]
        else:
            temp=C[i]+F[i]*math.ceil(temp/F[i])
    print(temp)

for i in range(N-1):
    calc(i)
print(0)

