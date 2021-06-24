H,W,N,M=map(int,input().split())
A=[]
B=[]
C=[]
D=[]

lighten=[[0 for _ in range(W+1)]for _ in range(H+1)]
for i in range(N):
    a,b=map(int,input().split())
    A.append(a)
    B.append(B)
    lighten[a][b]=2
for i in range(M):
    c,d=map(int,input().split())
    C.append(c)
    D.append(d)
    lighten[c][d]=9


# 2次元配列の転置は lighten=list(map(list,zip(*lighten)))


for h in range(1,H+1):
    nonzero=list(filter(lambda x:x not in (1,0),lighten[h]))
    i=0
    bright=False
    for w in range(1,W+1):
        if i<len(nonzero):
            if lighten[h][w] in (0,1):
                if bright or nonzero[i]==2:
                    lighten[h][w]=1
                    bright=True
            elif lighten[h][w]==2:
                bright=True
                i+=1
            elif lighten[h][w]==9:
                bright=False
                i+=1
        elif bright:
            lighten[h][w]=1

lighten=list(map(list,zip(*lighten)))

temp=H
H=W
W=temp
for h in range(1,H+1):
    nonzero=list(filter(lambda x:x not in (1,0),lighten[h]))
    i=0
    bright=False
    for w in range(1,W+1):
        if i<len(nonzero):
            if lighten[h][w] in (0,1):
                if bright or nonzero[i]==2:
                    lighten[h][w]=1
                    bright=True
            elif lighten[h][w]==2:
                bright=True
                i+=1
            elif lighten[h][w]==9:
                bright=False
                i+=1
        elif bright:
            lighten[h][w]=1

ans=0
for h in range(1,H+1):
    for w in range(1,W+1):
        if lighten[h][w] in (2,1):
            ans+=1
print(ans)
