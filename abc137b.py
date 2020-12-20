K,X=map(int,input().split())

for i in range(max(X-K+1,-1000000),min(X+K,1000000+1)):
    print(i,end=" ")
