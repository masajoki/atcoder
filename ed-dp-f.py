#動的計画法の練習
#蟻本にもでてきた

S=input() #s[i]
T=input() #t[j]
dp=[[0 for _ in range(len(T)+1)] for _ in range(len(S)+1)] # [i,j]までの共通部分列の長さの最大値

for i in range(1,len(S)+1):
    for j in range(1,len(T)+1):
        if S[i-1]==T[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i][j-1],dp[i-1][j])

#個数を算出する場合はこちら

# for k in range(1,len(T)+1):
#     if dp[i][k-1]!=dp[i][k]:
#         print(T[k-1],end="")

#文字列を算出する場合はこちら
## dpテーブルから逆に文字列を再現する

ans=[]
i=len(S)
j=len(T)
while i>0 and j>0:
    if S[i-1]== T[j-1]:
        ans.append(S[i-1])
        j-=1
        i-=1
    else:
        if dp[i-1][j]>=dp[i][j-1]:
            i-=1
        else:
            j-=1
ans.reverse()
print("".join(ans))
            

