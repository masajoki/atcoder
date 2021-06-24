N=int(input())
A=[]
for i in range(N):
    A.append(int(input()))

for i in range(N-1):
    if A[i+1]==A[i]:
        print("stay")
    elif A[i+1]>A[i]:
        print("up",A[i+1]-A[i])
    elif A[i+1]<A[i]:
        print("down",-A[i+1]+A[i])
