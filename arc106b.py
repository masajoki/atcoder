#連結グラフに分割して、連結グラフごとに合計がAとBで一致していれば、操作を行ってもトータルが変わらないから、必ずゴールまで行ける。
#最初に経路を拠点ごとに並べ替えて

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
marker=[]## チェックしたかどうか(visited)
forest=[] #連結グラフの入れ物(いきなり合計を出してしまっても良かった)
tree=[] #連結グラフのリスト

for i in range(N+1):
    marker.append(0)
    p=set()
    P.append(p)
marker[0]=1

for i in range(M):
    P[C[i]].add(D[i])
    P[D[i]].add(C[i])

for m in range(N+1):
    if marker[m] != 1:
        work=[] #queueとして使う
        tree=[]
        work.append(m)
        while len(work )> 0:
            pos=work.pop(0)
            if marker[pos]!=1:
                tree.append(pos)
                marker[pos]=1
                for i in P[pos]:
                    work.append(i)
        forest.append(tree)
for t in forest:
    sumA=0
    sumB=0
    for l in t:
        sumA+=A[l-1]
        sumB+=B[l-1]
    if sumA!=sumB:
        print("No")
        exit()

print("Yes")