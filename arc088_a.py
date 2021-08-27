X,Y=map(int,input().split())
ans=1
for i in range(1,61):
    X=X*2
    if X<=Y:
        ans+=1
print(ans)
