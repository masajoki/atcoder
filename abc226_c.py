from collections import deque
N=int(input())
T=[]
K=[]
A=[]
mastered=[0 for _ in range(N+1)]
for i in range(N):
    t=list(map(int,input().split()))
    T.append(t[0])
    K.append(t[1])
    A.append(t[2:])

ans=T[-1]
mastered[N]=1
q=deque()
for a in A[-1]:
    q.append(a)

while len(q)>0:
    v=q.popleft()
    if mastered[v]==0:
        ans+=T[v-1]
        mastered[v]=1
    else:
        continue
    for a in A[v-1]:
        if mastered[a]==0:
            q.append(a)
print(ans)

