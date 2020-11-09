N=int(input())
A=[]
B=[]
for n in range(N):
    a,b=map(int,input().split())
    A.append(a)
    B.append(b)

ans=0
for i in range(N):
    a=A[i]
    b=B[i]
    ans+=(b-a+1)*(a+b)/2

print(int(ans))