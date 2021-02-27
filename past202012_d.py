import decimal
N=int(input())
Si=[]
for i in range(N):
    s=input()
    si=decimal.Decimal(s)
    Si.append([si,s])
Si.sort(key=lambda x:(x[0],x[1]))
for s in Si:
    print(s[1])