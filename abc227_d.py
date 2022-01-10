from collections import deque
N,K=map(int,input().split())
A=list(map(int,input().split()))
A.sort()
q=deque()
qsum=0
ans=0
for i in range(N-K+1):
    if len(q)<K:
        q.append(A[i]-qsum)
        qsum+=A[i]-qsum
    else:
        t=q.popleft()
        ans+=t
        qsum-=t
        q.append(A[i]-qsum)
        qsum+=A[i]-qsum

print(ans+qsum)    
