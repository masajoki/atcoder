# Divide the problems
N=int(input())
D=list(map(int,input().split()))

D.sort()

if N%2==1:
    print(0)
    exit()
h=N//2

print(D[h]-D[h-1])