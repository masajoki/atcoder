#回答見てやった。
#場合の数を比べる。勝つパターンと、すべてのパターンで比較する。
K=int(input())
S=input()
T=input()

Scnt=[ 0 for _ in range(11)]
Tcnt=[ 0 for _ in range(11)]

for i in range(1,10):
    Scnt[i]=S.count(str(i))
    Tcnt[i]=T.count(str(i))

def Sscore(a):
    score=0
    for i in range(1,10):
        count=Scnt[i]
        if i==a:
            count+=1
        score+=i*(10**count)
    return score

def Tscore(a):
    score=0
    for i in range(1,10):
        count=Tcnt[i]
        if i==a:
            count+=1
        score+=i*(10**count)
    return score

ans=0

allpattern=(9*K-8)*(9*K-9) #すべてのパターン
okpattern=0 #OKなパターン
for i in range(1,10):
    ss=Sscore(i)
    for j in range(1,10):
        ts=Tscore(j)
        if ss>ts:
            if j!=i:
                okpattern+=(K-Scnt[i]-Tcnt[i])*(K-Tcnt[j]-Scnt[j])
            else:
                okpattern+=(K-Scnt[i]-Tcnt[i])*(K-Scnt[i]-Tcnt[i]-1)
            
ans=okpattern/allpattern
print(ans)




