#abc234_d.py
import heapq
N,K=map(int,input().split())
P=list(map(int,input().split()))
A=[]

for i in range(K):
    heapq.heappush(A,P[i])

for i in range(K,N):
    a=heapq.heappop(A)
    print(a)
    if P[i]>a:
        heapq.heappush(A,P[i])
    else:
        heapq.heappush(A,a)
print(heapq.heappop(A))        
