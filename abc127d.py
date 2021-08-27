import heapq
N,M=map(int,input().split())
A=list(map(int,input().split()))
B=[]
C=[]
CB=[[0,0] for _ in range(M)]
for i in range(M):
    b,c=map(int,input().split())
    CB.append([c,b])
CB.sort()
CB.reverse()
heapq.heapify(A)
for i in range(M):
    for j in range(CB[i][1]):
        t=heapq.heappop(A)
        if CB[i][0]>t:
            heapq.heappush(A,CB[i][0])
        else:
            heapq.heappush(A,t)
            break

print(sum(A))
