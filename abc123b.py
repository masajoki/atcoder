time=[]
ans=0
minmod=10
for i in range(5):
    t=int(input())
    time.append(t)
    if t%10==0:
        ans+=t//10
    else:
        ans+= t//10+1
        minmod=min(minmod,t%10)
if minmod!=0:
    print(ans*10-10+minmod)
else:
    print(ans*10)