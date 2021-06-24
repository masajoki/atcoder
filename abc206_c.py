N=int(input())
NumCount={}
Memo=[0 for _ in range(N)]
A=list(map(int,input().split()))
for i in range(N):
    if A[i] in NumCount:
        NumCount[A[i]]+=1
        Memo[i]=NumCount[A[i]]
    else:
        NumCount[A[i]]=1
        Memo[i]=NumCount[A[i]]

ans=0
for i in range(N):
    ans+=(N-(i+1)-NumCount[A[i]]+Memo[i])
print(ans)