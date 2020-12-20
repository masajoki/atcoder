N=int(input())
V=list(map(int,input().split()))
V.sort()
vtemp=V[0]
for i in range(1,N):
    vtemp=(V[i]+vtemp)/2
print(vtemp)

