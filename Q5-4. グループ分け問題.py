#Q5-4. グループ分け問題
#アルゴ式

parent=[]
groups=0
ans=[]

def init(N):
    parent=[i for i in range(N+1)]
    return parent

def root(x):
    if x==parent[x]:
        return x
    else:
        parent[x]=root(parent[x]) #親を更新しながら経路圧縮
        return parent[x]

#問題に対応するためにuniteを変更
def unite(x,y):
    global groups
    rx=root(x)
    ry=root(y)
    if rx!=ry:
        parent[rx]=ry #xの根rxをyの根ryにつけている
        groups-=1
    ans.append(groups)

def issame(x,y):
    rx=root(x)
    ry=root(y)
    return rx==ry


N,M=map(int,input().split())
groups=Ngroups=N
ans=[]
E=[[]for _ in range(N+1)]
parent=init(N)

for i in range(M):
    a,b=map(int,input().split())
    unite(a,b)



for a in ans:
    print(a)