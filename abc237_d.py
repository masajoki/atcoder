#abc237_d.py
N=int(input())
S=input()
A={}
A[-1]=[-1,-1]
A[0]=[-1,-1]
for i in range(N):
    left=A[i][0]
    right=A[i][1]

    RofLeft=A[left][1]
    LofRight=A[right][0]
    if S[i]=='L':
        A[i]=[i+1,A[i][1]]
        A[i+1]=[left,i]
        A[left][1]=i+1
        
    elif S[i]=='R':
        A[i]=[A[i][0],i+1]
        A[i+1]=[i,right]
        A[right][0]=i+1

start=-1
for i in range(N+1):
    if A[i][0]==-1:
        start=i

print(start,end=" ")
i=start
while True:
    if A[i][1]!=-1:
        print(A[i][1],end=" ")
        i=A[i][1]
    else:
        print()
        exit()