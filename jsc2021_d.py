N,P=map(int,input().split())
mod=10**9+7
ans=1
ans*=(P-1)*pow((P-2),N-1,mod)
print(ans%mod)