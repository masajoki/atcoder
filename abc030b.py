n,m=map(int,input().split())
sh=(n%12)*30+m*0.5
lh=m*6
print(min(abs(lh-sh),360-abs(lh-sh)))