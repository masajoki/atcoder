N,D,H=map(int,input().split())
minb=0
for i in range(N):
    d,h=map(int,input().split())
    temp=H-(H-h)/(D-d)*D
    minb=max(minb,temp)

print(minb)
