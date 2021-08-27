# AGC011B Colorful Creatures
N=int(input())
A=list(map(int,input().split()))
A.sort()
sumOfA=0
ng=0
for i in range(N-1):
    sumOfA+=A[i]
    if sumOfA*2<A[i+1]:
        ng=i+1
print(N-ng)




