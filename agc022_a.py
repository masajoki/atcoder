S=input()
slist=list(S)
cand=list("abcdefghijklmnopqrstuvwxyz")
used=[]
for s in S:
    cand.remove(s)
    used.append(s)

if len(cand)>0:
    print(S+min(cand))
    exit()
else:
    while(len(slist)>0):
        t=slist[-1]
        slist.remove(slist[-1])
        if len(cand)>0:
            cand.sort()
            for c in cand:
                if c > t:
                    print("".join(slist)+c)
                    exit()
        cand.append(t)
print(-1)