N = int(input())
S=input()
leftDebt=0
rightDebt=0
for s in S:
    if s=='(':
        rightDebt+=1
    else:
        if rightDebt>0:
            rightDebt-=1
        else:
            leftDebt+=1

print(leftDebt*"("+S+rightDebt*")")