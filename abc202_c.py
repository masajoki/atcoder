N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))
Count=[ 0 for _ in range(N+1)]

Acount=[ 0 for _ in range(N+1)]

for a in A:
    Acount[a]+=1

ans=0
BCcount=[0 for _ in range(N+1)]

for i in range(N):
    BCcount[B[C[i]-1]]+=1

for i in range(N+1):
    ans+=BCcount[i]*Acount[i]

print(ans)

