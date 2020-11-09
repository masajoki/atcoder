#連結グラフに分割して、連結グラフごとに合計がAとBで一致していれば、操作を行ってもトータルが変わらないから、必ずゴールまで行ける。
#最初に経路を拠点ごとに並べ替えて
from collections import deque
N,M=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=[]
D=[]


for i in range(M):
    c,d=map(int,input().split())
    C.append(c)
    D.append(d)

P=[] #作り直した拠点リスト
visited=[]## チェックしたかどうか(visited)
forest=[] #連結グラフの入れ物(いきなり合計を出してしまっても良かった)
tree=[] #連結グラフのリスト

for i in range(N+1):
    visited.append(False)
    p=set()
    P.append(p)
visited[0]=True

for i in range(M):
    P[C[i]].add(D[i])
    P[D[i]].add(C[i])

for m in range(N+1):
    if visited[m]==False:
        sumA=0
        sumB=0

        work=deque() #queueとして使う
        work.append(m)
        while len(work )> 0:
            pos=work.pop()
            if visited[pos]==False:
                sumA+=A[pos-1]
                sumB+=B[pos-1]
                visited[pos]=True
                for i in P[pos]:
                    work.append(i)
        if sumA!=sumB:
            print("No")
            exit()

print("Yes")