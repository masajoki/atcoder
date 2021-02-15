D,N=map(int,input().split())
ans=100**D
ans=ans*(N)
if N==100:
    print(ans+100**D)
else:
    print(ans)