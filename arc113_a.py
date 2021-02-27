K=int(input())
ans=0
for a in range(1,K+1):
    for b in range(1,K+1):
        if a*b>K:
            break
        for c in range(1,K+1):
            if a*b*c<=K:
                ans+=1
            else:
                break
print(ans)