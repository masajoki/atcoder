import heapq
Q=int(input())
Ope=[]
F=[]

addsum=0
for i in range(Q):
    q=input().split()
    p=int(q[0])
    x=0
    if len(q)==2:
        x=int(q[1])
    Ope.append((p,x))
    if p==2:
        addsum+=x



add=[addsum for _ in range(Q+1)]    
subs=[0 for _ in range(Q+1)]
currentadd=0

for i in range(Q-1,0,-1):
    p,x=Ope[i]
    if p==1 or p==3:
        add[i-1]=add[i]
    if p==2:
        add[i-1]=add[i]-x

for i in range(Q-1,0,-1):
    p,x=Ope[i]
    if p==1 or p==3:
        subs[i-1]=subs[i]
    if p==2:
        subs[i-1]=subs[i]+x


for i in range(Q):
    q=Ope[i]
    p=int(q[0])
    x=0
    if len(q)==2:
        x=int(q[1])
    if p==1:
        heapq.heappush(F,(x-currentadd,i))
        subs[i]=currentadd
    elif p==2:
        currentadd+=x
        subs[i]=currentadd
    elif p==3:
        temp=heapq.heappop(F)
        tx=temp[0]
        ti=temp[1]
        subs[i]=currentadd
        print(tx+add[i]-add[ti])
    




