N,M=map(int,input().split())
A=[]
B=[]
for i in range(M):
    a,b=map(int,input().split())
    A.append(a)
    B.append(b)
K=int(input())
CD=[]
for i in range(K):
    c,d=map(int,input().split())
    CD.append([c,d])


maxans=0
for i in range(2**K):
    ans=0
    T=[0 for _ in range(N+1)]
    for b in range(K):
        j=(i>>b&1)
        sara=CD[b][j]
        T[sara]=1
    for q in range(M):
        if T[A[q]]==1 and T[B[q]]==1:
            ans+=1
    
    maxans=max(maxans,ans)
    
print(maxans)
