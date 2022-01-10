N,D=map(int,input().split())
L=[]
R=[]
RL=[]

for i in range(N):
    l,r=map(int,input().split())
    L.append(l)
    R.append(r)
    RL.append((r,l))

RL.sort()

rt=RL[0][0]
punch=1
for i in range(N):
    if RL[i][1]<= rt +D-1:
        continue
    else:
        punch+=1
        rt=RL[i][0]

print(punch)    

