N=int(input())
x=[[-1 for _ in range(N)] for _ in range(N)] #x[証言した人(-1)][証言対象]=1:正直 0:不誠実
for i in range(N):
    A=int(input())
    for j in range(A):
        xt,yt=map(int,input().split())
        x[i][xt-1]=yt 

maxcount=0
for b in range(2**N): #正直な人の組み合わせ
    consistent=True
    count=0
    T=[-1 for _ in range(N)]    
    for c in range(N): #N桁シフトして取り出す.0からなので人証言対象とするには＋１する
        if (b >> c & 1) ==1:
            count+=1
            for i in range(N): #c番目の人は正直かチェック
                if T[i]==-1:
                    T[i]=x[c][i]
                elif x[c][i]==-1:
                    pass
                elif T[i]!=x[c][i]:
                    consistent=False
    for j in range(N): 
        if (b >> j & 1) ==1:
            if T[j]==1 or T[j]==-1:
                pass
            else:
                consistent=False
        else:
            if T[j]==0 or T[j]==-1:
                pass
            else:
                consistent=False
            
        
    if consistent==True:
        maxcount=max(count,maxcount)
print(int(maxcount))
