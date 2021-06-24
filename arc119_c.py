import copy

N=int(input())
S=list(input())
T=list(input())
if S.count("0")!=T.count("0"):
    print(-1)
    exit()
if S==T:
    print(0)
    exit()

S3=copy.deepcopy(S)
T3=copy.deepcopy(T)


# print("".join(T))

spos=0

ans=10**9

def finds(c): #ココがバグってるｗｗｗ
    global spos
    for i in range(spos,len(S)):
        if S[i]==c:
            if i+1<len(S):
                if S[i+1]==c:
                    continue
                else:
                    spos=i
                    return i
            else:
                spos=i
                return i
tempans=0
for i in range(len(S)):
    if S[i]!=T[i]:
        spos=max(i,spos)
        si=finds(T[i])
        S[si]=S[i]
        S[i]=T[i]
        tempans+=1
        print( "".join(S),tempans)
ans=min(ans,tempans)

spos2=N

def finds2(c):
    global spos2
    for i in range(spos2,-1,-1):
        if S3[i]==c:
            if i-1>=0:
                if S3[i-1]==c:
                    continue
                else:
                    spos2=i
                    return i
            else:
                spos2=i
                return i
tempans=0
print("".join(T))
print("".join(S3))

for i in range(len(S3)-1,-1,-1):
    if S3[i]!=T3[i]:
        spos2=min(i,spos2)
        si=finds2(T3[i])
        S3[si]=S3[i]
        S3[i]=T3[i]
        tempans+=1
        print( "".join(S3),tempans)
ans=min(ans,tempans)

if ans==10**9:
    print(-1)
else:
    print(ans)



