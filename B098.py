N,M,T,K=map(int,input().split())

ruiseki=[0 for _ in range(N)]

favs=[]

for i in range(M):
    fav=list(map(int,input().split()))
    favs.append(fav)


ans=[["no",0] for _ in range(N)]

for i in range(T):
    for j in range(N):
        ruiseki[j]+=favs[i][j]
        if ruiseki[j]>=K and ans[j][0]=="no":
            ans[j][0]="yes"
            ans[j][1]=i+1

for i in range(T,M):
    for j in range(N):
        ruiseki[j]-=favs[i-T][j]
        ruiseki[j]+=favs[i][j]
        if ruiseki[j]>=K and ans[j][0]=="no":
            ans[j][0]="yes"
            ans[j][1]=i+1

for i in range(N):
    print(ans[i][0],ans[i][1])
