N,A,B=map(int,input().split())
rest=N%(A+B)
ans=A*(N//(A+B))

if rest <=A:
    ans+=rest
else:
    ans+=A
print(ans)