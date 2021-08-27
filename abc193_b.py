N=int(input())
A=[]
P=[]
X=[]
S=[]
ans=10**10
for i in range(N):
    a,p,x=map(int,input().split())
    if x-a>0:
        ans=min(ans,p)

if ans==10**10:
    print(-1)
else:
    print(ans)