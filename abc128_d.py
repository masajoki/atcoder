N,K=map(int,input().split())
V=list(map(int,input().split()))
W=[]
for v in V:
    if v>0:
        W.append(v)
    else:
        W.append(0)
        W.append(0)


for i in range(K):
    tempmax=0
    for j in range(i+1):
        temp=0
        left=i-j
        right=N-j
        temp+=sum(W[:left])
        temp+=sum(W[right:])
        tempmax=max(tempmax,temp)
        # print("i,j,L,R,temp",i,j,left,right,temp)
print(tempmax)
