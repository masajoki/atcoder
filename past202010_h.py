N,M,K=map(int,input().split())
S=[]
for  i in range(N):
    s=list(map(int,list(input())))
    S.append(s)

ans=0

def check(i,j,n,S):
    A=[0 for _ in range(10)]
    for h in range(i,i+n):
        for w in range(j,j+n):
            if 0<=h<N and 0<=w<M:
                A[S[h][w]]+=1
            else:
                return False
    A.sort(reverse=True)
    if A[0]+K>=n**2:
        return True

for n in range(1,min(N,M)+1):
    for i in range(N-n+1):
        for j in range(M-n+1):
            if check(i,j,n,S):
                ans=max(ans,n)


print(ans)



