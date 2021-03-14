S=input()
repeat=False
lastChr=""
lastUsedChr=""
lastUsedChrCount=0
nonUsedChrCount=0
ABC=list("abcdefghijklmnopqrstuvwxyz")
chardict={}
charcount={}
slen=len(S)
for abc in ABC:
    chardict[abc]=[0 for _ in range(slen)]
    charcount[abc]=0
ans=0

lastErasePos=slen
for i in range(len(S)-1,-1,-1):
    charcount[S[i]]+=1
    for abc in ABC:
        chardict[abc][i]=charcount[abc]

for i in range(len(S)-1,-1,-1):
    s=S[i]
    if s==lastChr:
        if lastErasePos!=slen:
            if i+2<slen:
                ans+=len(S)-i-2-lastErasePos+2 -chardict[s][i+2]+chardict[s][lastErasePos]
            else:
                ans+=len(S)-i-2-lastErasePos+2 +chardict[s][lastErasePos]
        else:
            if i+2<slen:
                ans+=len(S)-i-2 -chardict[s][i+2]
            else:
                ans+=len(S)-i-2
        lastErasePos=i+2
    lastChr=s
print(ans)

#なんかグシャグシャになって終わったー