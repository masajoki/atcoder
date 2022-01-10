N=int(input())
V=[0 for _ in range(N+1)]
for i in range(N-1):
    a,b=map(int,input().split())
    V[a]+=1
    V[b]+=1

if max(V)==N-1:
    print("Yes")
else:
    print("No")

