#和を最初に計算しておいて、しゃくとり法？で計算時間を短くする。
N,K=map(int,input().split())
A=list(map(int,input().split()))

imosu=[0 for _ in range(N)]
tempsum=0
ans=0
startpoint=0
for i in range(N):
    tempsum+=A[i]
    imosu[i]=tempsum

for i in range(N):
    if imosu[i]>=K:
        startpoint=i
        break


shakutori=0
for j in range(startpoint,N):
    for i in range(shakutori,j+1):
        t=imosu[j]-imosu[i]+A[i]
        if t<K:
            ans+=i
            shakutori=i-1
            break
        elif i==j:
            shakutori=j
            ans+=j+1
print(ans)
