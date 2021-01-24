# from collections import deque
X=int(input())
# temp=deque()
# temp.append(0)
# for i in range(1,X+1):
#     last=""
#     l=len(temp)
#     for j in range(l):
#         k=temp.popleft()
#         if k==last:
#             continue
#         temp.append(k+i)
#         temp.append(k)
#         temp.append(k-1*i)
#         pass

# temps=list(set(temp))
# temps.sort()
# print(temps)

import math
ans=math.ceil((-1+(1+8*X)**0.5)/2)
print(ans)