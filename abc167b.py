A,B,C,K=map(int,input().split())
ans=0
if K>=A:
    ans+=A
    K-=A
else:
    print(K)
    exit()
if K>=B:
    K-=B
else:
    print(ans)
    exit()

print(ans-K)



