import heapq
N=int(input())
A=list(map(int,input().split()))
heapq.heapify(A)



while len(A)>1:
    t1=heapq.heappop(A)
    t2=heapq.heappop(A)
    if t1!=t2 and t2%t1!=0:
        t2=t2%t1
        heapq.heappush(A,t2)
    heapq.heappush(A,t1)
print(t1)

