from collections import deque
Q=int(input())
queue=deque()
for i in range(Q):
    t,x=map(int,input().split())
    if t==1:
        queue.appendleft(x)
    elif t==2:
        queue.append(x)
    else:
        print(queue[x-1])
