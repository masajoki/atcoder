N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
temp=0
for i in range(N):
    temp+=A[i]*B[i]
if temp==0:
    print("Yes")
else:
    print("No")
