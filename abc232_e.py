#abc232_e
#abc232_e
H,W,K=map(int,input().split())
a,b,c,d=map(int,input().split())
mod=998244353
temp=pow((H+W-4),K,mod)
ans=temp%mod
print(ans)
