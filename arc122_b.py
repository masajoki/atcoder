N=int(input())
A=list(map(int,input().split()))
A.sort()
allA=sum(A)
sumA=[A[0]]
for i in range(1,len(A)):
    sumA.append(sumA[i-1]+A[i])
ans=float("inf")
for i in range(N):
    temp=allA-sumA[i]
    
    ans=min(temp/(N-2*(N-i-1)),ans)

print(ans)
