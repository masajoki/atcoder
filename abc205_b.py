N=int(input())
A=list(map(int,input().split()))
A.sort()
for i in range(1,len(A)+1):
    if i!=A[i-1]:
        print("No")
        exit()
print("Yes")

