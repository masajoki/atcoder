import itertools
N=input()
L=list(map(int,input().split()))
L.sort()
C=list(itertools.combinations(L,3))
ans=0
for a in C:
    if a[0]==a[1] or a[0]==a[2] or a[1]==a[2]:
        continue
    else:
        # print(a)
        if (a[0]+a[1])>a[2]:
            ans+=1
print(ans)
