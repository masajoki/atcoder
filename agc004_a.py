A,B,C=map(int,input().split())
a1,a2,b1,b2,c1,c2=[0,0,0,0,0,0]
if A%2==0:
    a1=A//2
    a2=a1
else:
    a1=A//2
    a2=A//2+1

if B%2==0:
    b1=B//2
    b2=b1
else:
    b1=B//2
    b2=B//2+1

if C%2==0:
    c1=C//2
    c2=c1
else:
    c1=C//2
    c2=C//2+1

ans=10**50
ABC=A*B*C
for a in (a1,a2):
    ans=min(ans,abs(((A-a)*B*C)-a*B*C))
for b in (b1,b2):
    ans=min(ans,abs((A*(B-b)*C)-A*b*C))
for c in (c1,c2):
    ans=min(ans,abs((A*B*(C-c))-A*B*c))

print(ans)