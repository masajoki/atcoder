#abc234_b.py
N=int(input())
X=[]
Y=[]
for i in range(N):
    x,y=map(int,input().split())
    X.append(x)
    Y.append(y)

ans=0
for i in range(N):
    for j in range(N):
        temp=(X[i]-X[j])**2 + (Y[i]-Y[j])**2
        ans=max(ans,temp)
print(ans**0.5)

