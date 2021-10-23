N=int(input())
A=[]
B=[]

userzougen=[]
zaiseki=[0 for _ in range(N+10)]
for i in range(N):
    a,b=map(int,input().split())
    A.append(a)
    B.append(b)
    userzougen.append((a,1))
    userzougen.append((a+b,-1))

userzougen.sort()

lastday=userzougen[0][0]
todayusers=0
for day,inout in userzougen:
    if lastday==day:
        todayusers+=inout
    else:
        zaiseki[todayusers]+=(day-lastday)
        todayusers+=inout
        lastday=day

for i in range(1,N+1):
    print(zaiseki[i])


