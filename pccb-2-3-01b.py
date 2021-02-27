#メモ化するナップサック問題（再帰）
N=int(input())
Limit=int(input())
dp=[[0 for _ in range(Limit+1)] for _ in range(N+1) ]
W=[]
V=[]
for i in range(N):
    w,v=map(int,input().split())
    W.append(w)
    V.append(v)

#i番目以降の荷物から、重さの総和がj以下となるように選ぶ
def rec(i,j): #価値の総和を返す
    if dp[i][j]>0:
        #すでに調べたことがあるなら、その結果を返す
        return dp[i][j]

    if i==N:
        res=0
    elif j<W[i]:
        #この荷物は入らない
        res=rec(i+1,j)
    else:
        #この荷物は入る
        #荷物が入るならば、荷物を入れる場合と入れない場合の療法を試す
        ireru=rec(i+1,j-W[i])+V[i] #荷物を入れる場合、重さの総和を荷物の重さ分引き下げる
        irenai=rec(i+1,j)
        res=max(ireru,irenai)
        dp[i][j]=res #メモ化
    return res

print(rec(0,Limit))