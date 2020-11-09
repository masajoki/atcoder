x,n=map(int,input().split())
Ps=list(map(int,input().split()))
Ps.sort()

table=[0]*102

for i in Ps:
    table[i]=1

ans=0
min=101
for i in range(0,102):
   if table[i]==0:
       temp=abs(x-i)
       if temp<min:
           min=temp
           ans=i
print(ans)
