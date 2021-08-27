N=int(input())
A=list(map(int,input().split()))
minA=min(A)
maxA=max(A)
minans=9999999999
for i in range(minA,maxA+1):
    ans=0
    for a in A:
        ans+=(a-i)**2
    minans=min(ans,minans)
print(minans)
