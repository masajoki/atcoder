N,D=map(int,input().split())
ans=0
for _ in range(N):
    x,y=map(int,input().split())
    if (x**2+y**2)**0.5 <= D:
        ans+=1
print(ans)