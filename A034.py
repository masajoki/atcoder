N,X=map(int,input().split())
C=[]
for _ in range(N):
    C.append(int(input()))

ans=[]
for i in range(2**N):
    kashinum=0
    hiyou=0
    for b in range(N):
        if i>>b&1:
            kashinum+=1
            hiyou+=C[b]
        
    if hiyou<=X:
        ans.append((kashinum,X-hiyou))

ans.sort(reverse=True)
kashinum=ans[0][0]

temp=10**10
for a in ans:
    if a[0]==kashinum:
        temp=min(temp,a[1])
    else:
        break
print(temp)