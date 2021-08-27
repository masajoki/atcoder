N=int(input())
A=list(map(int,input().split()))
Ai=[]
for i in range(1,N+1):
    Ai.append([i,A[i-1]])

Ai.sort(key=lambda x:x[1],reverse=True)

for ai in Ai:
    print(ai[0])
