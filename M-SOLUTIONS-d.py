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
bottom=A[0]
peak=A[0]
trend="NONE"

if peak < A[1]:
    trend="UP"
    stock=money//A[0]
    money=money-stock*A[0]    
elif bottom > A[1]:
    trend="DOWN"

for i in range(1,N):
    # print(stock,money,trend)
    if peak < A[i] and trend=="UP":
        peak=A[i]
    elif bottom > A[i] and trend=="DOWN":
        bottom=A[i]
    elif bottom < A[i] and trend=="DOWN":
        #底打ち
        stock=money//bottom
        money=money-stock*bottom
        peak=A[i]
        trend="UP"
    elif peak > A[i] and trend=="UP":
        #天井
        money=money+stock*peak
        stock=0
        bottom=A[i]
        trend="DOWN"
print(stock*peak+money)

