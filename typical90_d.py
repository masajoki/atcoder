H,W=map(int,input().split())
A=[]
for i in range(H):
    a=list(map(int,input().split()))
    A.append(a)
Hsum=[0 for _ in range(H)]
Wsum=[0 for _ in range(W)]

for h in range(H):
    Hsum[h]=sum(A[h])

for w in range(W):
    t=0
    for h in range(H):
        t+=A[h][w]
    Wsum[w]=t

B=[[0 for  _ in range(W) ]for _ in range(H)]
for i in range(H):
    for j in range(W):
        B[i][j]=Hsum[i]+Wsum[j]-A[i][j]

        print(B[i][j], end=" ")
    print()

