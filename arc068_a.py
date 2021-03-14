x=int(input())
m=x%11
ans=x//11*2
if 1<=m<=6:
    ans+=1
elif m>6:
    ans+=2
print(ans)

#5,6だけ出し続ける