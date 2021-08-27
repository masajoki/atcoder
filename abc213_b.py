N=int(input())
A=list(map(int,input().split()))
T=[]
for i in range(N):
    T.append((A[i],i))

T.sort(reverse=True)
print(T[1][1]+1)
