import decimal
N=int(input())
X=[]
Y=[]

jpy=0
btc=0
for i in range(N):
    x,y=input().split()
    if y=="JPY":
        jpy+=decimal.Decimal(x)
    else:
        btc+=decimal.Decimal(x)

print(jpy+btc*decimal.Decimal(380000.0))
