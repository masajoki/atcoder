N=int(input())
polls={}
S=[]
for i in range(N):
    S.append(input())

for s in S:
    if s not in polls:
        polls[s]=1
    else:
        polls[s]+=1

maxpoll=max(polls.values())
ans=[]
for k,v in polls.items():
    if v==maxpoll:
        ans.append(k)
ans.sort()
for a in ans:
    print(a)