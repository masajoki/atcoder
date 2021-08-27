H,N=map(int,input().split())
A=list(map(int,input().split()))
SUM=0
for a in A:
    SUM+=a

if H <= SUM:
    print('Yes')
else:
    print('No')
