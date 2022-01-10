from collections import deque
N,Q=map(int,input().split())
maeushiro=[0 for _ in range(N+1)]
ushiromae=[0 for _ in range(N+1)]

query=[]
for _ in range(Q):
    q=list(map(int,input().split()))
    query.append(q)

for q in query:
    command=q[0]
    if command==1:
        mae=q[1]
        ushiro=q[2]
        maeushiro[mae]=ushiro
        ushiromae[ushiro]=mae
    elif command==2:
        mae=q[1]
        ushiro=q[2]
        maeushiro[mae]=0
        ushiromae[ushiro]=0
    elif command==3:
        tq=deque()
        

