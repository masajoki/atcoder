#030 - K Factors（★5） 
N,K=map(int,input().split())
Count=[0 for _ in range(N+1)]
ans=0
for i in range(2,N+1):
    if Count[i]!=0: #すでにカウントされていれば素数ではない。０なら素数。賢い…
        continue
    else:
        for j in range(i,N+1,i): #エラトステネスの篩と同じ。素数は事前に算出しておく必要がない。
            Count[j]+=1


for i in range(1,N+1):
    if Count[i]>=K:
        ans+=1

print(ans)
