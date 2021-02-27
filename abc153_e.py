# ABC153E E - Crested Ibis vs Monster 
# DPの問題
#Hモンスターの体力
#N魔法の種類(魔法は何度使っても良い)
H,N=map(int,input().split())

A=[]
B=[]
for i in range(N):
    a,b=map(int,input().split())
    A.append(a)
    B.append(b)
f_inf=float("inf")

#dp[魔法の種類][与えたダメージ]= 与えるのに最低必要な消費魔力量
dp=[[f_inf for _ in range(H+1)] for _ in range(N+1)]

dp[0][0]=0
for i in range(N):
    for j in range(H+1):
        damage=A[i]
        usedMP=B[i]
        if j>=A[i]:
            dp[i+1][j]=min(dp[i][j],dp[i+1][j-damage]+usedMP)
        else:
            dp[i+1][j]=min(dp[i][j],usedMP)
print(dp[N][H])

#重複を許すナップサック問題と完全に同じ
#重複を許さない場合との違いは、dp[i][j-damage]+usedMP が dp[i+1][j-damage]+usedMP となっただけ。
# それだけで何故という感じがする。
