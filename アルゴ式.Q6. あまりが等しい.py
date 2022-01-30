#アルゴ式.Q6. あまりが等しい.py
A,B=map(int,input().split())
# A mod x = r
# B mod x = r
# A - B mod x = 0


def div_count(N):
    from collections import defaultdict
    A=defaultdict(int)
    for i in range(2,int(N**0.5+1)):
        while N%i==0:
            N//=i
            A[i]+=1
    if N!=1:
        A[N]=1
    ans=1
    for i,c in A.items():
        ans*=(c+1)
    return ans

if A<B:
    A,B=B,A


print(div_count(A-B))


