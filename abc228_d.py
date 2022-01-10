from collections import deque
N=2**20
A=[-1]*(N+1)
Q=int(input()) ##0<=x<=10**5
T=[] #1か2
X=[] #0<=x<=10**18
for i in range(Q):
    t,x=map(int,input().split())
    T.append(t)
    X.append(x)
temp=[deque() for _ in range(N)]
queue=deque()
for i in range(Q):
    t=T[i]
    x=X[i]
    if t==1:
        h=x
        hmodn=h%N
        temp[hmodn].append(x)
        queue.append(hmodn)
    elif t==2:
        while len(queue)>0:
            hmond=queue.popleft()
            tempq=temp[hmodn]
            while len(tempq)>0:
                tempx=tempq.popleft()
                if A[hmodn]==-1:
                    A[hmodn]=tempx
                else:
                    tempq.appendleft(tempx)
                        

