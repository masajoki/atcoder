N=int(input())
XI=[]
X=list(map(int,input().split()))
for i in range(N):
    XI.append((X[i],i))
XI.sort()

B=[]
for i in range(N):
    x=X[i]
    mid=N//2
    median=0
    if x<=XI[mid][0]-1:
        median=XI[N//2]
    else:
        median=XI[N//2-1]
    B.append(median)

for b in B:
    print(b[0])