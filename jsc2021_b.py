N,M=map(int,input().split())
T=[0 for _ in range(10000)]
A=[]
B=[]
A=list(map(int,input().split()))
B=list(map(int,input().split()))

for i in range(N):
    T[A[i]]+=1
for i in range(M):
    T[B[i]]+=1

for i in range(len(T)):
    if T[i]==1:
        print(i, end=" ")
print()