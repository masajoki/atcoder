import heapq
R,C=map(int,input().split())
A=[]
B=[]
for i in range(R):
    A.append(list(map(int,input().split())))
for i in range(R-1):
    B.append(list(map(int,input().split())))

dist=[ [ float('inf') for _ in range(C+1) ]for _ in range(R+1)]
seen=[ [ False for _ in range(C+1) ]for _ in range(R+1)]

edgelist=[]
dist[0][0]=0
seen[0][0]=True
r=0
c=0
heapq.heappush(edgelist,(A[r][c],r,c+1))
heapq.heappush(edgelist,(B[r][c],r+1,c))

while len(edgelist):
    edge=heapq.heappop(edgelist)
    cost=edge[0]
    r,c=edge[1],edge[2]
    if seen[r][c]:
        continue
    dist[r][c]=min(cost,dist[r][c])
    t=dist[r][c]
    seen[r][c]=True
    if c+1<C and not seen[r][c+1]:
        heapq.heappush(edgelist,(t+A[r][c],r,c+1))
    if 0<=c-1 and not seen[r][c-1]:
        heapq.heappush(edgelist,(t+A[r][c-1],r,c-1))
    if r+1<R  and not seen[r+1][c]:
        heapq.heappush(edgelist,(t+B[r][c],r+1,c))
    for i in range(1,r+1):
        if 0<=r-i and not seen[r-i][c]:
            heapq.heappush(edgelist,(t+i+1,r-i,c))

print(dist[R-1][C-1])
