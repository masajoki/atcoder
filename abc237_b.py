import numpy as np
H,W=map(int,input().split())
A=[]
for i in range(H):
    a=list(input().split())
    A.append(a)

ary=np.array(A)
tary=np.transpose(ary)

for t in tary:
    print(*t)