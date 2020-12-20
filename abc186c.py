N=int(input())
ans=0
for i in range(1,N+1):
    numc=str(i).count('7')
    numo=oct(i).count('7')
    if numc == numo ==0:
        ans+=1
print(ans)