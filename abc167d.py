N,K=map(int,input().split())
temp=list(map(int,input().split()))
A=[1]
for t in temp:
    A.append(t)

visited=[0 for _ in range(N+1)]

looplength=0
pathbeforeloop=0
pathrest=0

loopbegin=99999999

last=0
for i in range(K+1):
    if visited[A[last]]==0:
        pathbeforeloop+=1
        visited[A[last]]+=1
    elif visited[A[last]]==1:
        looplength+=1
        visited[A[last]]+=1
    elif visited[A[last]]==2:
        loopbegin=A[last]
        pathrest=(K-pathbeforeloop)%looplength
        last=A[last]
        break
    last=A[last]

for i in range(pathrest):
    last=A[last]
print(last)
