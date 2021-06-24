
S=list(input())
N=len(S)+1
A=[ 0 for _ in range(N)]

temp=0
for i in range(N-1):
    if S[i]=='<':
        temp+=1
        A[i+1]=temp
    else:
        temp=0

temp=0
for i in range(N-2,-1,-1):
    if S[i]=='>':
        temp+=1
        A[i]=max(A[i],temp)
    else:
        temp=0

print(sum(A))

