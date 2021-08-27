H,W=map(int,input().split())
N=int(input())
A=list(map(int,input().split()))

T=[[0 for _ in range(W)] for _ in range(H)] 


a=0
rev=False
for i in range(H):
    if rev==False:
        for j in range(W):
            if A[a]==0:
                a+=1
            T[i][j]=a
            A[a]-=1
        rev=True
    elif rev==True:
        for j in range(W-1,-1,-1):
            if A[a]==0:
                a+=1
            T[i][j]=a
            A[a]-=1
        rev=False

for t in T:
    for i in t:
        print(i+1,end=" ")
    print()
