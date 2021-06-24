H,W=map(int,input().split())
A=[]
for i in range(H):
    A.append(list(input()))


Wwhite=[1 for _ in range(W)]
Hwhite=[1 for _ in range(H)]

for i in range(H):
    for j in range(W):
        if A[i][j]=='#':
            Wwhite[j]=0
            Hwhite[i]=0



for i in range(H):
    if Hwhite[i]==1:
        continue
    else:
        for j in range(W):
            if Wwhite[j]==1:
                continue
            else:
                print(A[i][j],end="")
    print()

