A=list(map(int,input().split()))
ans=0
for a in A:
    ans=max(ans,sum(A)-a)

print(ans)