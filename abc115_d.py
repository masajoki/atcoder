N,X=map(int,input().split())

burger=[1]
putty=[1]
p=1
b=1
for i in range(N):
    b=b*2+3
    p=p*2+1
    burger.append(b) #レベルごとのburgerの厚さ
    putty.append(p) #レベルごとのパティの枚数

burger.reverse() #レベルが大きい順
putty.reverse() #レベルが大きい順

if X<=N: #Nより小さければバンズしかない
    print(0)
    exit()
if burger[0]-N+1<=X<=burger[0]: # 最大レベルのバンズ分を食べきっている
    print(putty[0])
    exit()

ans=0
eaten=0
for i in range(1,N):
    if X-eaten==2+burger[1]:
        ans+=putty[i]+1
        break
    elif X-eaten > 2+burger[i]:
        ans+=putty[i]+1
        eaten+=2+burger[i]
    else:
        X-=1
        # print("--"+str(i))
ans+=min(X,3)

print(ans)