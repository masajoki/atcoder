# # D - Banned K  / 
# # 3<=N<=2*10**5
# # 1<=Ai<=N
# # 整数
# K: 1,2,3,...,N に対して、
# K番目のボールを除いたN-1個のボールから
# 同じ番号が書かれているボールを2つ選びだ方法の数を求める

import math
numcount=[0 for _ in range(2*10**5+10)]

N=int(input())
A=list(map(int,input().split()))
for i in range(N):
   numcount[A[i]]+=1

sumcombi=0
def combi(j):
    if j>=2:
        # t=math.factorial(j)/(2*math.factorial(j-2))
        t=j*(j-1)/2
        return int(t)
    else:
        return 0

for i in range(1,N+1):
    temp=combi(numcount[i])
    sumcombi+=temp

for i in range(N):
    temp=combi(numcount[A[i]]-1)
    temp2=combi(numcount[A[i]])
    print(sumcombi-temp2+temp)