N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

Asur=0
Bsur=0
for i in range(N):
    Asur+=max(0,(B[i]-A[i])//2)
    Bsur+=max(0,(A[i]-B[i]))

if Asur>=Bsur:
    print("Yes")
else:
    print("No")

