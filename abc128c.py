#なんかごちゃごちゃしてるけどbit全探索するだけ
N,M=map(int,input().split())
S=[]
P=[]
for _ in range(M):
    T=list(map(int,input().split()))
    U=[]
    for i in range(T[0]):
        U.append(T[i+1])
    S.append(U)
P=list(map(int,input().split()))


Spat=[[] for _ in  range(2**N)]
for i in range(2**N):
    St=[0 for _ in range(N)]
    for b in range(N):
        s = (i >> b & 1)
        St[-1 -1*b]=s
    Spat[i]=St.copy()


temp=0
ans=0
for spat in Spat: # スイッチの点灯パターン
    lightson=True
    for p in range(M): # Mこのパターン
        s=S[p] # スイッチの組
        temp=0
        for t in s: #t：スイッチの番号
            temp+=spat[t-1]
        if temp %2 != P[p]:
            lightson=False
    if lightson==False:
        continue
    else:
        ans+=1
print(ans)





