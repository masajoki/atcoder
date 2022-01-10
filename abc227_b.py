N=int(input())
S=list(map(int,input().split()))
candidate=set()
for a in range(1,333):
    for b in range(1,333):
        candidate.add(4*a*b+3*a+3*b)
ans=0
for s in S:
    if s not in candidate:
        ans+=1

print(ans)
