N=int(input())
P=list(map(int,input().split()))

difference=0

for i in range(N):
    difference+=abs(i-P[i]+1)

if difference%2!=0:
    print("NO")
else:
    print("YES")
