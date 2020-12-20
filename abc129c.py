N,M=map(int,input().split())
A=[]
for i in range(M):
    A.append(int(input()))
Steps=[ -1 for _ in range(N+10)]
Steps[0]=1
Steps[1]=1
for a in A:
    Steps[a]=0

for i in range(2,N+10):
    if Steps[i]!=0:
        Steps[i]=Steps[i-1]+Steps[i-2]
print(Steps[N]%1000000007)