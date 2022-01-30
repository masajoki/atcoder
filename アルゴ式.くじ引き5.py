#アルゴ式.くじ引き5.py
N,K=map(int,input().split())
ans=1
for i in range(K):
    ans*=(N-i-1)/(N-i)
print(1-ans)