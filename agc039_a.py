S=input()
scnt=[]
K=int(input())
tmp=[[S[0],1]]
ans=0
for i in range(1,len(S)):
    if tmp[-1][0]==S[i]:
        tmp[-1][1]+=1
    else:
        tmp.append([S[i],1])
if len(tmp)>=2 and tmp[0][0]==tmp[-1][0]:
    for i in range(1,len(tmp)-1):
        ans+=K*(tmp[i][1]//2)
    ans+=tmp[0][1]//2
    ans+=tmp[-1][1]//2
    ans+=(K-1)*((tmp[0][1]+tmp[-1][1])//2)
elif len(tmp)==1:
    ans=tmp[0][1]*K//2
else:
    for i in range(len(tmp)):
        ans+=K*(tmp[i][1]//2)

print(ans)


