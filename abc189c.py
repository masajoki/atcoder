N=int(input())
    
A=list(map(int,input().split()))
if N==1:
    print(A[0])
    exit()

ans=0
for i in range(N):
    minA=A[i]
    for j in range(i,N):
        minA=min(minA,A[j])
        ans=max(ans,minA*(j-i+1))
print(ans)

