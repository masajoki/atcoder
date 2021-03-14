H,W=map(int,input().split())
S=[]
T0=[]
T1=[]
T2=[]
T3=[]
for _ in range(H):
    S.append(input())

for _ in range(H):
    t=input()
    T0.append(t)
    tr=list(t)
    tr.reverse()
    T1.append(tr)

T1.reverse()
T2=list(zip(*T0))
T2.reverse()
T3=list(zip(*T1))
T3.reverse()



for h in H:
    for w in W:
        