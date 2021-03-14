N,A,B=map(int,input().split())
S=[]
for i in range(N):
    s=int(input())
    S.append(s)

Smax=max(S)
Smin=min(S)
if Smax!=Smin:
    P=B/(Smax-Smin)
else:
    print(-1)
    exit()

Q=A-(P*sum(S)/N)
print(P,Q)