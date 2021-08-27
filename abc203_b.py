N,K=map(int,input().split())
ans=[]
for i in range(1,N+1):
    for j in range(1,K+1):
        t=str(i)+"0"+str(j)
        ans.append(int(t))
print(sum(ans))