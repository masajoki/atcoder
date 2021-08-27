N,K=map(int,input().split())
A=list(map(int,input().split()))
Asort=sorted(A)
rest=K-N*(K//N)

C={}
for i in range(N):
    C[Asort[i]]=K//N

for j in range(rest):
    C[Asort[j]]+=1

for a in A:
    print(C[a])
