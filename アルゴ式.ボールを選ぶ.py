#ボールを選ぶ.py
N,M=map(int,input().split())

ans=1
for i in range(M):
    ans*=(N-i)

temp=1
for j in range(1,M+1):
    temp*=j

print(ans//temp)


