N=int(input())
ansStr=""
tempStr=""
for i in range(30,-1,-1):
    div=2**i
    if N//div==1:
        N-=div
        tempStr=tempStr+"1"
    else:
        tempStr=tempStr+"0"


for i in range(len(tempStr)):
    if i%2==0:
        ansStr=tempStr[-i]+ansStr
    else:
        if tempStr[-i]=="0":
            ansStr="00"+ansStr
        else:
            ansStr="11"+ansStr
print(ansStr)    

