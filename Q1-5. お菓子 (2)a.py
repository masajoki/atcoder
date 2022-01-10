N=int(input())
ans=0
while N!=0:
    if N%3==0:
        N//=3
        ans+=1
    else:
        N-=1
        ans+=1
print(ans)
