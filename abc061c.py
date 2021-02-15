N,K=map(int,input().split())
AB=[]
for i in range(N):
    a,b=map(int,input().split())
    AB.append([a,b])

AB.sort(key=lambda x:x[0])

for i in range(N):
    K-=AB[i][1]
    if K<=0:
        print(AB[i][0])
        break