N=int(input())
S=input()

last=""
maxcount=0
temp=0
for s in S:
    if s=='.':
        temp+=1
    else:
        maxcount=max(maxcount,temp)
        temp=0

leftcount=0
for i in range(N):
    if S[i]=='.':
        leftcount+=1
    else:
        break
rightcount=0
for i in range(N-1,-1,-1):
    if S[i]=='.':
        rightcount+=1
    else:
        break


print(leftcount,rightcount+max(0,maxcount-leftcount-rightcount))