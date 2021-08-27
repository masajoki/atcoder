N,K=map(int,input().split())
dic={}
for i in range(N):
    s=input()
    if s in dic:
        dic[s]+=1
    else:
        dic[s]=1

diclist=list(dic.items())

diclist.sort(key=lambda x : x[1], reverse=True)

t=set()
c=0
for i in (K-2,K-1,K):
    if 0<=i<len(diclist):
        t.add(diclist[i][1])
        c+=1

if len(t)==c:
    print(diclist[K-1][0])
else:
    print("AMBIGUOUS")