n,m=map(int,input().split())
#n:偶数
#m:奇数
ans=0
if n>=2:
    ans+=n*(n-1)/2
if m>=2:
    ans+=m*(m-1)/2

print(int(ans))