import heapq
#heapq使うと勝手にソートしてくれる。
N,M=map(int,input().split())
A=[]
B=[]
heapAB=[]

for i in range(N):
    a,b=map(int,input().split())
    heapq.heappush(heapAB,[a,b])

ans=0
drinks=0
for i in range(N):
    ab=heapq.heappop(heapAB)
    if ab[1]>=(M-drinks):
        ans+=(ab[0]*(M-drinks))
        print(ans)
        exit()
    elif ab[1]<(M-drinks):
        ans+=ab[1]*ab[0]
        drinks+=ab[1]

