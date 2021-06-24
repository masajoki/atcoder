from collections import deque
N=int(input())
A=[]
C=[]
cnt={}
cnt['R']=0
cnt['B']=0
cnt['G']=0

AC=[]
for i in range(2*N):
    a,c=input().split()
    cnt[c]+=1
    A.append(int(a))
    C.append(c)
    AC.append([int(a),c])

even=''
if cnt['R']%2== 0 and cnt['B']%2==0 and cnt['G']%2==0:
    print(0)
    exit()
elif cnt['R']%2==0:
    even='R'
elif cnt['B']%2==0:
    even='B'
elif cnt['G']%2==0:
    even='G'


nonEvens=[]
for ac in AC:
    if ac[1]!=even:
        nonEvens.append(ac)

ans=float("inf")

for i in range(len(nonEvens)-1):
    if nonEvens[i][1]!=nonEvens[i+1][1]:
        if ans>nonEvens[i+1][0]-nonEvens[i][0]:
            ans=nonEvens[i+1][0]-nonEvens[i][0]

Candidate=[]

for i in range(2*N-1):
    if AC[i][1]!=AC[i+1][1]:
        if AC[i][1]==even:
            Candidate.append((abs(AC[i][0]-AC[i+1][0]),AC[i][1]))
        if AC[i+1][1]==even:
            Candidate.append((abs(AC[i][0]-AC[i+1][0]),AC[i+1][1]))

Candidate.sort(reverse=True)

temp=float("inf")
if Candidate[0][1]==Candidate[1][1]:
    temp=Candidate[0][0]+Candidate[2][0]
else:
    temp=Candidate[0][0]+Candidate[1][0]

print(min(ans,temp))



