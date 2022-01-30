#アルゴ式.変わったサイコロ3.py

N,X=map(int,input().split())
P=list(map(int,input().split()))

ans=0

for i in range(1,N+1):
    if 1<=X-i<=N:
        ans+=(P[i-1]*P[X-i-1]/10000)
print(ans)
