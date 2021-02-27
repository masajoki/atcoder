N=int(input())
B=list(map(int,input().split()))
ans=[]
for j in range(N):
    if len(B)>0:
        for i in range(len(B)-1,-1,-1):
            if B[i]==i+1:
                del B[i]
                ans.append(i+1)
                break
if len(B)==0:
    ans.reverse()
    for a in ans:
        print(a)
else:
    print(-1)
