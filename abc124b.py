N=int(input())
H=list(map(int,input().split()))
ans=1
maxmt=0
for i in range(N-1):
    maxmt=max(maxmt,H[i])
    if maxmt<=H[i+1]:
        ans+=1

print(ans)