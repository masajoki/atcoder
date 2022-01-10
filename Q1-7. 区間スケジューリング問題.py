N=int(input())
TS=[]
for i in range(N):
    s,t=map(int,input().split())
    TS.append((t,s,i))
ans=0
TS.sort()
ts=0
sp=0
for c in range(10010):
    for d in range(ts,N):
        t,s,i=TS[d]
        if t==c and s>=sp:
            ans+=1
            ts=d+1
            sp=t
            break
        elif t>c:
            break
print(ans)






