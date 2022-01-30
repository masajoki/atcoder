#アルゴ式.チーム分け1.py
N,A,B,_=map(int,input().split())


ans=0
def func(N,M):
    ans=1
    for i in range(M):
        ans*=(N-i)

    temp=1
    for j in range(1,M+1):
        temp*=j

    return (ans//temp)

print(func(N,A)*func((N-A),B))

