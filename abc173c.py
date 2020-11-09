#abc173c.py
# C - H and V
H,W,V=list(map(int,input().split()))
S=[]
for i in range(H):
    S.append(input().replace('.','0').replace('#','1'))

print(S)

for i in range(V):
    