#アルゴ式.チーム分け1.py
N,M,_=map(int,input().split())

ans=1
for i in range(M):
    ans*=(N-i)

temp=1
for j in range(1,M+1):
    temp*=j

print(ans//temp)


