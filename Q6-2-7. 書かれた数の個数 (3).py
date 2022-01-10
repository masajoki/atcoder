N,X,Y=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
AB=A+B
AB.sort()
abs=set()
for a in AB:
    abs.add(a)

ans=0
for ab in range(1,N+1):
    if ab not in abs:
        ans+=1
print(ans)