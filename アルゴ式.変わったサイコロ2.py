#アルゴ式.変わったサイコロ2.py

N,M=map(int,input().split())
P=list(map(int,input().split()))
D=list(map(int,input().split()))
ans=1

for i in range(M):
    ans=ans*P[D[i]-1]/100
print(ans)