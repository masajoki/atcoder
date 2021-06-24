import heapq
W,H=map(int,input().split())
P,Q=[],[]
PQ=[]
for i in range(W):
    p=int(input())
    heapq.heappush(PQ, (p,'W'))
for i in range(H):
    q=int(input())
    heapq.heappush(PQ, (q,'H'))

ans=0
while len(PQ)>0:
    c=heapq.heappop(PQ)
    if c[1]=='H':
        ans+=c[0]*(W+1)
        H-=1
    else:
        ans+=c[0]*(H+1)
        W-=1
print(ans)

