N,M=map(int,input().split())
A=list(map(int,input().split()))
import heapq

heapA=[]
for a in A:
    heapq.heappush(heapA,-1*a)

for m in range(M):
    temp=-1*heapq.heappop(heapA)
    temp =temp//2
    heapq.heappush(heapA,-1*temp)

print(-1*sum(heapA))