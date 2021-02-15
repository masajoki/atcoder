N,X,Y=map(int,input().split())

R=2
Cs=[]
aC=[]
ans=[ 0 for k in range(N)]

def combination(startn):
    if len(aC)==R:
        Cs.append(aC.copy()) #copy必須
        return
    for i in range(startn,N+1):
        aC.append(i)
        combination(i+1)
        aC.pop()

combination(1) #1-2, 1-3, ..., 7-8, 8-9 みたいにペアを作る

for c in Cs:
    a=c[0]
    b=c[1]
    distance=min(b-a,abs(a-X)+1+abs(b-Y))
    ans[distance]+=1

for a in range(1,N):
    print(ans[a])
