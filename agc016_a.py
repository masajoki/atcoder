S=list(input())
ABC="abcdefghijklmnopqrstuvwxyz"
S.reverse()
maxinitgap={}
maxgap={}
for abc in ABC:
    maxinitgap[abc]=0
    maxgap[abc]=0
    
for abc in ABC:
    gap=0
    initgap=True
    for i in range(len(S)):
        if S[i]!=abc:
            gap+=1
        else:
            if initgap:
                maxinitgap[abc]=gap
                initgap=False
            else:
                maxgap[abc]=max(maxgap[abc],gap)
            gap=0
    if initgap:
        maxinitgap[abc]=gap
    else:
        maxgap[abc]=max(maxgap[abc],gap)

minans=999999999999
for abc in ABC:
    ans=0
    ans=max(maxinitgap[abc],maxgap[abc])
    minans=min(minans,ans)
print(minans)

    