"""
1000円
株
N日間の株価

2日〜80日
株価は100~200円

"""
N=int(input())
A=list(map(int,input().split()))

stock=0
money=1000

for i in range(1,N):
    #上がってたら前日の価格との差分を毎日もらう
    if A[i-1] < A[i]:
        money=money+ (A[i]-A[i-1]) * (money//A[i-1]) 
print(money)

