N=int(input())
A=[0]
for i in range(N):
    A.append(int(input()))

temp=1
for i in range(1,N+1):
    temp=A[temp]
    if temp == 2:
        print(i)
        exit()
print(-1)