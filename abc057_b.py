n,m=map(int,input().split())
AB=[]
CD=[]
for i in range(n):
    a,b=map(int,input().split())
    AB.append((a,b))

for i in range(m):
    c,d=map(int,input().split())
    CD.append((c,d))

for i in range(n):
    minmanhattan=9999999999
    ans=9999999999
    for j in range(m):
        manhattan=abs(AB[i][0]-CD[j][0])+abs(AB[i][1]-CD[j][1])
        if minmanhattan>manhattan:
            ans=j
            minmanhattan=manhattan
    print(ans+1)