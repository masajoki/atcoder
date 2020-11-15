#これはもらうDPのパターン

N=int(input())
h=list(map(int,input().split()))
cost=[999999999 for _ in range(N)]


def calccost(i,j):
    return abs(h[i]-h[j])

cost[0]=0 
for i in range(N):
    for j in [-1,-2]: #1つ前と2つ前
        if (i+j)>=0: 
            cost[i]=min(cost[i],cost[i+j]+calccost(i,i+j)) #比較
print(cost[-1]) #ゴールのコスト