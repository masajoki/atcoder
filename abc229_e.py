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
    E[a].append(b)

temp=[0 for _ in range(N+1)]

trees=0
for i in range(N-1,0,-1):
    trees+=1
    for b in E[i+1]:
        if not issame(i+1,b):
            unite(i+1,b)
            trees-=1
    temp[i]=trees

print(*temp[1:])
