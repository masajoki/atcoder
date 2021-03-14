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


right=startpoint
leftstart=0
for right in range(startpoint,N):
    for left in range(leftstart,right+1):
        t=imosu[right]-imosu[left]+A[left]
        if t<K:
            ans+=left
            leftstart=left-1
            break
        elif left==right:
            ans+=left+1
            leftstart=left
            break
print(ans)
