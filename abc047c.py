S=input()
last=S[0]
ans=0
for s in S:
    if s!=last:
        last=s
        ans+=1
print(ans)
