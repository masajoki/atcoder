#累積和を使って頑張る解法
N,Q=map(int,input().split())
A=list(map(int,input().split()))
B=[]
Bsum=[]
K=[]
Ans=[ 0 for _ in range(Q)]
for i in range(Q):
    k=int(input())
    K.append([k,i])

B.append(A[0]-1)
for i in range(1,len(A)):
    B.append(A[i]-A[i-1]-1)

Bsum.append(B[0])
for i in range(1,len(B)):
    Bsum.append(Bsum[i-1]+B[i])

K.sort()

bi=0
for kt in K:
    k=kt[0]
    i=kt[1]
    while bi<len(Bsum)-1 and k>Bsum[bi]:
        bi+=1

    if bi==0:
        Ans[i]=0+k
    elif k==Bsum[bi]:
        Ans[i]=A[bi-1]+k-Bsum[bi-1]
    elif Bsum[bi]>k:
        Ans[i]=A[bi-1]+(k-Bsum[bi-1])
    else:
        Ans[i]=A[bi]+(k-Bsum[bi])

for a in Ans:
    print(a)