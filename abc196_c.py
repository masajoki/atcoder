N=int(input())
ans=0
for i in range(1,N):
    t=10**len(str(i))*i+i
    if t<=N:
        ans+=1
    else:
        break
print(ans)
