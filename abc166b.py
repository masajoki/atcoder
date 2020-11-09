N,K=map(int,input().split())

answer=[0]*(N+5)
for k in range(K):
    D=int(input())
    A=list(map(int,input().split()))
    for a in A:
        answer[a]=1

for a in answer:
    N-=a
print(N)