N=int(input())
A=list(map(int,input().split()))
daisum=0
maxheight=A[0]
for  i in range(1,N):
    if A[i]<maxheight:
        daisum+=maxheight-A[i]
    else:
        maxheight=A[i]
print(daisum)
