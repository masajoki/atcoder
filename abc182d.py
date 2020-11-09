N=int(input())
A=list(map(int,input().split()))
moveeffect=[0]
maxmoveeffect=[0]
onePathMovePos=[0]
highestmovedpos=[0]
finalmovedpos=[0]

for a in A:
    moveeffect.append(a)
for i in range(1,len(A)+1):
    onePathMovePos.append(onePathMovePos[i-1]+moveeffect[i])
    
    if onePathMovePos[i]>0 and onePathMovePos[i]>maxmoveeffect[i-1]:
        maxmoveeffect.append(onePathMovePos[i])
    else:
        maxmoveeffect.append(maxmoveeffect[i-1])
    
    finalmovedpos.append(finalmovedpos[i-1]+onePathMovePos[i])
    highestmovedpos.append(finalmovedpos[i-1]+maxmoveeffect[i])

print(max(highestmovedpos))


