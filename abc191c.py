H,W=map(int,input().split())
S=[]
for i in range(H):
    S.append(input())

kado=0
for i in range(1,H):
    for j in range(1,W):
        t=0
        if S[i][j]=='#':
            t+=1
        if S[i-1][j]=='#':
            t+=1
        if S[i][j-1]=='#':
            t+=1
        if S[i-1][j-1]=='#':
            t+=1
        if t%2==1:
            kado+=1
print(kado)


