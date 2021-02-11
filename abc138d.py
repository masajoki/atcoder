import sys 
sys.setrecursionlimit(10**6) 

N,Q=map(int,input().split())
Path=[[] for _ in range(N+10)] #Path
Score=[0 for _ in range(N+10)] #Score
Ope=[ 0 for _ in range(N+10)] #operations
Visited=[ False for _ in range(N+10)]
for i in range(N-1):
    a,b=map(int,input().split())
    Path[a].append(b)
    Path[b].append(a)

for i in range(Q):
    p,x=map(int,input().split())
    Ope[p]+=x

def dfs(root,score):
    global Visited
    Visited[root]=True
    ts=score+Ope[root]
    Score[root]+=ts
    for p in Path[root]:
        if Visited[p]:
            continue
        dfs(p,ts)

Visited[1]=True
dfs(1,0)

for i in range(1,N+1):
    print(Score[i],end=" ")
print()


#pathがルートから遠い方から記述されている場合があるので、両向きのパスを保存しておいて、訪問済みを管理しないといけない
# setrecursionlimitをやらないと RecursionError: maximum recursion depth exceeded してしまう
# CythonじゃないとTLEしてしまう
# でもやってることはあってた！ for loop で同じことをしたいものだ