from collections import deque
N=int(input())
temp=list(map(int,input().split()))

P=[ int() for _ in range(N+1)]

for i in range(1,N+1):
    P[i]=temp[i-1]

sumdif=0
Dif=[ int() for _ in range(N+1)]#iの本来からの位置のずれ、本来の位置にあれば0,右にあればプラス
for i in range(1,N+1):
    Dif[i]=i-P[i]
    sumdif+=abs(P[i]-i)
    #本来の位置にあるやつが一つでもあればアウト
    if Dif[i]==0:
        print(-1)
        exit()

#ずれの合計が一定でなければアウト
if sumdif != (N-1)*2:
    print(-1)
    exit()

tobechanged=set()

count=0
queue=deque()
for i in range(1,N):
    queue.append(i)

while len(queue)>0:
    i=queue.popleft()    
    if Dif[i]<0 and Dif[i+1]>0:
        temp=P[i]
        P[i]=P[i+1]
        P[i+1]=temp
        Dif[i]=i-P[i]
        Dif[i+1]=i-P[i+1]
        print(i)
        count+=1
        if count==N-1:
            exit()
    else:
        queue.append(i)