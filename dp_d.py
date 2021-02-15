N,Wmax=map(int,input().split())

W=[]
V=[]

for i in range(N):
    w,v=map(int,input().split())
    W.append(w)
    V.append(v)

# i番目のアイテムを選んだときの、重さがw以下のときの価値の最大値を格納する
dp=[[0 for _ in range(Wmax+1)] for _ in range(N+1)]

for i in range(N):
    for j in range(Wmax+1):
        if j - W[i] >=0:
            #i番目のアイテムを選んだ場合
            dp[i+1][j]=max(dp[i][j-W[i]]+V[i],dp[i][j])
        else:
            #i番目のアイテムを選ばない場合
            dp[i+1][j]=dp[i][j]

print(dp[N][Wmax])
