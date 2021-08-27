N,X=map(int,input().split())
S="P"
for i in range(N):
    S="BP"+S+"PB"
ans=0
for i in range(X):
    if S[i]=="P":
        ans+=1
print(ans)
