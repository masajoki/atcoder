N=int(input())
A=list(map(int,input().split()))
fours=0
twos=0
others=0
for a in A:
    if a%4==0:
        fours+=1
    elif a%2==0:
        twos+=1
    else:
        others+=1

if twos>0 and fours>=others:
    print("Yes")
elif twos==0 and fours>=(others-1):
    print("Yes")
else:
    print("No")

