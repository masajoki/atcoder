S=input()
Scnt=0
Tcnt=0
for s in S:
    if s=='S':
        Scnt+=1
    else:
        if Scnt>0:
            Scnt-=1
        else:
            Tcnt+=1
print(Scnt+Tcnt)
