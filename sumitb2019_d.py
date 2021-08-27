import re
N=int(input())
S=input()
ans=0
posi=[[] for _ in range(10)]
for i in range(N):
    s=int(S[i])
    posi[s].append(i)


for i in range(0,1000):
    temp=format(i,"03d")
    a,b,c=map(int,temp)
    apos=-1
    bpos=-1
    cpos=-1
    if len(posi[a])>0:
        apos=posi[a][0]
    else:
            continue
    if len(posi[b])>0:
        for t in posi[b]:
            if t>apos:
                bpos=t
                break
        else:
            continue
        
    if len(posi[c])>0:
        for u in posi[c]:
            if u>bpos:
                cpos=u
                break
        else:
            continue
    if apos!=-1 and bpos!=-1 and cpos!=-1:
        ans+=1
print(ans)

#動的計画法でもできるらしい