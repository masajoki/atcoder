#Q5-3. 連結成分の最小値.py
# Union Findの利用

# アルゴ式

parent=[]

def init(N):
    parent=[i for i in range(N+1)]
    return parent

def root(x):
    if x==parent[x]:
        return x
    else:
        parent[x]=root(parent[x]) #親を更新しながら経路圧縮
        return parent[x]

def unite(x,y):
    rx=root(x)
    ry=root(y)
    if rx==ry:
        return
    else:
        parent[rx]=ry #xの根rxをyの根ryにつけている

def issame(x,y):
    rx=root(x)
    ry=root(y)
    return rx==ry


N,M=map(int,input().split())
E=[[]for _ in range(N+1)]
parent=init(N)

for i in range(M):
    a,b=map(int,input().split())
    unite(a,b)

ans={}
for i in range(N):
    temp=root(i)
    if temp in ans.keys():
        ans[temp]=min(ans[temp],i)
    else:
        ans[temp]=i
for i in range(N):
    print(ans[root(i)])

    
