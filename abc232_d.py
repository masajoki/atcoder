#abc232_d
from collections import deque
H,W=map(int,input().split())
Q=deque()
C=[]
for i in range(H):
    c=input()
    C.append(c)

Q.append((0,0,1)) #h,w,steps
Steps=[[0 for _ in range(W)] for _ in range(H)]

while len(Q)>0:
    h,w,steps=Q.pop()
    Steps[h][w]=max(Steps[h][w],steps)
    if h+1<H and C[h+1][w]==".":
        if Steps[h+1][w] < steps+1:
            Q.append((h+1,w,steps+1))
    if w+1<W and C[h][w+1]==".":
        if Steps[h][w+1] < steps+1:
            Q.append((h,w+1,steps+1))

ans=0
for i in range(H):
    ans=max(ans,max(Steps[i]))
print(ans)