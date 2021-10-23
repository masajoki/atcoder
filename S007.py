from collections import deque
SI=input()
NumQ=deque()
Par=deque()
Str=deque()

ABC="abcdefghijklmnopqrstuvwxyz"
NUM="0123456789"
PAR="()"
ans={}
for a in ABC:
    ans[a]=0

NumQ.append(1)
numswitch=False
i=0
while i <len(SI):
    numtempstr=[]
    level=0
    if i>=len(SI):
        break

    if SI[i] in ABC:
        if numswitch==True:
            mtemp=NumQ.pop()
            mtempPrev=NumQ.pop()
            ans[SI[i]]+=mtemp*mtempPrev
            NumQ.append(mtempPrev)
            numswitch=False
            i+=1
        else:
            mtemp=NumQ.pop()
            ans[SI[i]]+=mtemp
            NumQ.append(mtemp)    
            i+=1
    if i>=len(SI):
        break
    while SI[i] in NUM:
        numtempstr.append(SI[i])
        i+=1
    if len(numtempstr)>0:
        lastnum=int("".join(numtempstr))
        NumQ.append(lastnum)
        numswitch=True

    if i>=len(SI):
        break
    if SI[i] == "(":
        if numswitch==True:
            lastemp=NumQ.pop()
            beforelast=NumQ.pop()
            newmulti=lastemp*beforelast
            NumQ.append(beforelast)
            NumQ.append(newmulti)
            numswitch=False
        i+=1
    if i>=len(SI):
        break
    if SI[i] ==")":
        if len(NumQ)>0:
            NumQ.pop()
        numswitch=False
        i+=1        
for a in ABC:
    print(a,ans[a])
