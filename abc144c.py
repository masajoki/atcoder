# from collections import deque 
N=int(input())

# queue=deque([[1,1]])
# while queue:
#     now=queue.popleft()
#     if (now[0]*now[1])==N:
#         print(now[0]+now[1]-2)
#         break
#     elif now[0]*now[1]<N:
#             queue.append([now[0]+1,now[1]])
#             queue.append([now[0],now[1]+1])
#     else:
#         break

import math
start=math.ceil(math.sqrt(N))
for i in range(start,0,-1):
    if N%i==0:
        print(i+N//i-2)
        break