N=int(input())
S=input()
flg=False
rightIgeta=0
leftWhite=0
for i in range(N):
    if S[i]=='.':
        leftWhite+=1
    else:
        break
for i in range(N-1,-1,-1):
    if S[i]=='#':
        rightIgeta+=1
    else:
        break

print(min(S[leftWhite:N-rightIgeta].count("."),S[leftWhite:N-rightIgeta].count("#")))