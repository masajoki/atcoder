S=list(input())
from collections import deque
Q=deque()

ans=0

def calc():
    zero=False
    global Q,ans
    while len(Q)>0:
        a=Q.popleft()
        if a=='0':
            zero=True
    if not zero:
        ans+=1
    
for s in S:
    if s=="+":
        calc()
    else:
        Q.append(s)

calc()

print(ans)