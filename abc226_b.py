N=int(input())
A=set()
for i in range(N):
    t=tuple(map(int,input().split()))
    A.add(t[1:])
print(len(A))