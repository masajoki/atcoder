S=input()
atcoder="ACGT"
ans=0
maxans=0
for s in S:
    if s in atcoder:
        ans+=1
        maxans=max(ans,maxans)
    else:
        ans=0
print(maxans)
