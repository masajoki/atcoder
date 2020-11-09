N,M=map(int,input().split())
A=list(map(int,input().split()))
A.sort()
A.reverse()
totalvote=sum(A)
# print(totalvote)
for i in range(M):
    if A[i]<(totalvote/(4*M)):
        print("No")
        exit()
print("Yes")