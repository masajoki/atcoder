N=int(input())
A=list(map(int,input().split()))
C={}
ans=0
for a in A:
    if a in C:
        C[a]+=1
    else:
        C[a]=1

for i in C.keys():
    if C[i]>i:
        ans+=C[i]-i
    if C[i]<i:
        ans+=C[i]
print(ans)
