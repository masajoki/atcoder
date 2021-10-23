N,M=map(int,input().split())
A=[]

for j in range(M):
    a=int(input())
    A.append(a)


ans=0
for i in range(N):
    score=100
    for j in range(M):
        m=int(input())
        temp=abs(A[j]-m)
        if temp>30:
            score-=5
        elif 0<=temp<=5:
            score-=0
        elif temp<=10:
            score-=1
        elif temp<=20:
            score-=2
        elif temp<=30:
            score-=3
    ans=max(ans,score)
print(ans)
        
