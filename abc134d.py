N=int(input())
A=list(map(int,input().split()))
Ans=[0 for _ in range(N+1)]
for n in range(N-1,-1,-1):
    temp=0
    for i in range((n+1)*2-1,N,n+1):
        temp+=Ans[i]
    if temp&2!=A[n]:
        Ans[n]=1

ans=0
for i in range(N+1):
    if Ans[i]==1:
        ans+=1
print(ans)
for i in range(N+1):
    if Ans[i]==1:
        print(i+1,end=" ")
print()
    

        

