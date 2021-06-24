N=int(input())
L=list(map(int,input().split()))
L.sort()

S=sum(L[:-1])
if L[-1]<S:
    print("Yes")
else:
    print("No")