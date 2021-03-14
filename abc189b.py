N,X=map(int,input().split())
X=X*100
for i in range(N):
    v,p=map(int,input().split())
    X-=v*p
    if X<0:
        print(i+1)
        exit()
print(-1)
