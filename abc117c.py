N,M=map(int,input().split())
X=list(map(int,input().split()))
X.sort()
Xdiff=[]
for i in range(M-1):
    Xdiff.append(abs(X[i+1]-X[i]))

Xdiff.sort()

ans=0
for i in range(M-N):
    ans+=Xdiff[i]

print(ans)
