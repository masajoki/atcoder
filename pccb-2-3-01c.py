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

def solve():
    for i in range(N-1,-1,-1):
        for j in range(Limit+1):
            if j<W[i]:
                dp[i][j]=dp[i+1][j]
            else:
                dp[i][j]=max(dp[i+1][j],dp[i+1][j-W[i]]+V[i])

solve()
print(dp[0][Limit]) 