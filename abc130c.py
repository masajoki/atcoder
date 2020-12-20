W,H,x,y=map(int,input().split())
if x==W/2 and y==H/2:
    ans2=1
else:
    ans2=0
print(H*W/2,ans2)