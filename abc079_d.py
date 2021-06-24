#ワーシャルフロイド法で解いてみる
H,W=map(int,input().split())
Cs=[]
for _ in range(10):
    c=list(map(int,input().split()))
    Cs.append(c)

As=[]
for _ in range(H):
    a=list(map(int,input().split()))
    As.append(a)

for k in range(10):
    for i in range(10):
        for j in range(10):
            Cs[i][j]=min(Cs[i][j], Cs[i][k] + Cs[k][j] )

ans=0
for h in range(H):
    for w in range(W):
        if As[h][w] == -1:
            continue
        else:
            ans += Cs[As[h][w]][1]

print(ans)
