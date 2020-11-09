#机A, B
#机A：N冊の本が縦積み, B: M冊
#このやりかたではまちがっていたよ
import collections

N,M,K=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

dqA=collections.deque()
dqB=collections.deque()

for a in A:
    dqA.append(a)
for b in B:
    dqB.append(b)


totaltime=0
answer=0
while totaltime <= K:
    if len(dqA) > 0 and len(dqB)> 0:    
        a=dqA.popleft()
        b=dqB.popleft()
        if a<=b:
            dqB.appendleft(b)
            totaltime += a
        else:
            dqA.appendleft(a)
            totaltime += b
    elif len(dqA)>0:
        a=dqA.popleft()
        totaltime += a
    elif len(dqB)>0 :
        b=dqB.popleft()
        totaltime += b
    elif len(dqA)==0 and len(dqB)==0:
        print(answer)
        exit()
    if totaltime > K:
        print(answer)
        exit()
    else:
        answer+=1

        

