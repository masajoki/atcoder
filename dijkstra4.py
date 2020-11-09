import heapq
def dijkstra(edges,num_v):
    dist=[float('inf')]*num_v
    dist[0]=0
    q=[]
    heapq.heappush(q,[0,0])