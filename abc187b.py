N=int(input())
X=[]
Y=[]
for i in range(N):
    x,y=map(int,input().split())
    X.append(x)
    Y.append(y)

ans=0
for i in range(N-1):
    for j in range(i,N):
        if (X[j]-X[i] )==0:
            continue
        katamuki=(Y[j]-Y[i] )/ (X[j]-X[i])
        if -1 <= katamuki<= 1:
            ans+=1

print(ans)
