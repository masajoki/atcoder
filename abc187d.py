N=int(input())
A=[]
B=[]
TakAdv=[]
AokiVote=0
ans=0
for i in range(N):
    a,b=map(int,input().split())
    A.append(a)
    B.append(b)
    TakAdv.append(2*a+b)
    AokiVote+=a

TakAdv.sort()
TakAdv.reverse()

for a in TakAdv:
    AokiVote-=a
    ans+=1
    if AokiVote<0:
        print(ans)
        break