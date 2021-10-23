import heapq
N,C,K=map(int,input().split()) #パイプ本数、予算、作るパイプの長さ
B=[] #太さ
P=[] #価格
BP=[]
BPI=[]

for i in range(N):
    b,p=map(int,input().split())
    if p>C:
        continue

    B.append(b)
    P.append(p)
    BP.append((b,p))
    heapq.heappush(BPI,(-b,-p,i))

N=len(B)
temp=0

PickedPBI=[]
RestBPI=[]

for i in range(K):
    p=heapq.heappop(BPI)
    temp-=p[1]
    heapq.heappush(PickedPBI,(p[1],p[0],p[2]))

for i in range(K,N):
    p=heapq.heappop(BPI)
    heapq.heappush(RestBPI,p)

for i in range(N):
    if temp>C:
        p,b,i=heapq.heappop(PickedPBI)
        temp+=p #格納してるのがマイナスだから

        r=heapq.heappop(RestBPI)
        rb,rp,ri=r
        temp-=rp #格納してるのがマイナスだから
        heapq.heappush(PickedPBI,(rp,rb,ri))

ans=-1000000

for p in PickedPBI:
    ans=max(ans,p[1])

print(-ans)    
