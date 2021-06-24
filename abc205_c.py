A,B,C=map(int,input().split())

big=5
small=3

tempA=0
tempB=0
tempC=0
if A==B:
    print("=")
    exit()

if A<0:
    tempA=-1
elif A>0:
    tempA=1
if B<0:
    tempB=-1
elif B>0:
    tempB=1

if abs(A)> abs(B):
    tempA=big*tempA
    tempB=small*tempB
elif abs(A)< abs(B):
    tempA=small*tempA
    tempB=big*tempB
else:
    tempA=small*tempA
    tempB=small*tempB

if abs(C)>10:
    if C%2 == 0:
        tempC=2
    else:
        tempC=3
else:
    tempC=C

if tempA**tempC<tempB**tempC:
    print("<")
elif tempA**tempC>tempB**tempC:
    print(">")
else:
    print("=")
