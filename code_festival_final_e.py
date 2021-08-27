N=int(input())
A=list(map(int,input().split()))
dp=["" for _ in range(N+2)]

start=N
for i in range(1,N):
    if A[i]<A[i-1]:
        dp[i]="T"
        start=i
        break
    elif A[i]>A[i-1]:
        dp[i]="B"
        start=i
        break



for i in range(start,N):
    if dp[i-1]=="d" or dp[i-1]=="T":
        if A[i]<=A[i-1]:
            dp[i]="d"
        else:
            dp[i]="B"
    elif dp[i-1]=="u" or dp[i-1]=="B":
        if A[i]>=A[i-1]:
            dp[i]="u"
        else:
            dp[i]="T"

if dp[N-1] in ("B","u"):
    dp[N]="T"
elif dp[N-1] in ("d","T"):
    dp[N]="B"

if dp.count("B")==0 or dp.count("T")==0:
    print(0)
elif dp.count("B")==1 and dp.count("T")==1: 
    print(0)
else:
    print(dp.count("T")+dp.count("B"))