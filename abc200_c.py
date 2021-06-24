N=int(input())
A=list(map(int,input().split()))
T={}
for a in A:
    t=a%200
    if t in T.keys():
        T[t]+=1
    else:
        T[t]=1

ans=0
for t in T.values():
    ans+=(t*(t-1))//2

print(ans)