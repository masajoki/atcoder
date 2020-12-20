L,R=map(int,input().split())
maxans=2018*2017
ans=maxans
for i in range(L, min(L+ 2019,R)):
    for j in range(i+1, min(L+2019,R+1)):
        temp=(i*j)%2019
        if ans>temp:
            ans=temp
print(ans)