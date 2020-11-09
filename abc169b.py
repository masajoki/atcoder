N=int(input())
A=list(map(int,input().split(' ')))
ans=1
calcneeded=1

for a in A:
    if (a == 0):
        print(0)
        exit()
    
    if (calcneeded == 1):
        ans*=a
    
    if (ans > 10**18):
        calcneeded=0

if (ans > 10**18):
    print(-1)
else:
    print(ans)


