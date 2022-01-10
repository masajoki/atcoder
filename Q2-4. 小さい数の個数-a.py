#Q2-4. 小さい数の個数-a.py
#簡単な内容ならbisect使ったほうが簡単だね
#アルゴ式
#2分探索

import bisect

N,M=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split())) 
A.sort()
ans=[]
for i in range(M):
    T=B[i]
    j=bisect.bisect_right(A,T)
    if j<N and A[j]==T: 
        ans.append(j+1)
    else:
        ans.append(j)

for a in ans:
    print(a)
