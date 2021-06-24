N,K=map(int,input().split())
A=list(map(int,input().split()))

BallNum=[0 for _ in range(N+1)]
for a in A:
    BallNum[a]+=1

BallNum.sort(reverse=True)
ans=0
for i in range(K, N+1):
    ans+=BallNum[i]
print(ans)



