N=int(input())
A=[]
for i in range(N):
    A.append(int(input()))

bottom=A[0]
ans=1
for i in range(1,N):
    if A[i]<=bottom:
        bottom=A[i]
        ans+=1
print(ans)