N,K=map(int,input().split())
rest=N
digits=[0]

for i in range(30,0,-1):
    digits.append(rest//K**i)
    rest=rest%K**i
digits.append(rest)

count=0
for i in range(len(digits)):
    if digits[i]!=0:
        print(len(digits)-i)
        break
