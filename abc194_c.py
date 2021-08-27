N=int(input())
A=list(map(int,input().split()))
# ans=0
# for i in range(N-1):
#     for j in range(i,N):
#         ans+=(A[i]-A[j])**2
# print(ans)

sumA=sum(A)
sumAq=0
for a in A:
    sumAq+=a**2

ans=0
print(N*(sumAq)-sumA**2)

#式変形で頑張った。 (a-b)^2 + (b-c)^2 + (c-a)^2 
# = (a^2+b^2+c^2)*N - (a+b+c)^2 みたいになる  