import collections
N,M,K=map(int,input().split())
MyFavs=list(map(int,input().split()))
Review=[]
for i in range(M):
    r=list(map(int,input().split()))
    Review.append(r)

MyFavStores=set()
MyNonVisitStores=collections.deque()
Friends=set()
for i in range(N):
    if MyFavs[i]>=3:
        MyFavStores.add(i)
    elif MyFavs[i]==0:
        MyNonVisitStores.append(i)

for i in range(M):
    aRev=Review[i]
    likeness=0
    for j in range(N):
        if aRev[j]>=3 and j in MyFavStores:
            likeness+=1
        if likeness >=K:
            Friends.add(i)
            break

Candiddate=set()
for f in Friends:
    for s in MyNonVisitStores:
        if Review[f][s]>=3:
            Candiddate.add(s)

if len(Candiddate)==0:
    print("no")
else:
    ans=list(Candiddate)
    for i in range(len(ans)):
        if i==len(ans)-1:
            print(ans[i]+1)
        else:
            print(ans[i]+1,end=" ")