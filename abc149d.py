N,K=map(int,input().split())
R,S,P=map(int,input().split())
T=list(input())
# 動的計画法使っても良さそうだけど単にループ回すだけでおK
# K手前と同じ手が出せないので、step=Kでループする。
# 同じ手が繰り返されなければ全部勝てば良く、
# 繰り返される場合、1つ目を勝ち、2目は捨て、3つ目は勝ち、とすればよい。
score=0
for i in range(K):
    last='o'
    for j in range(i,N,K):
        t=T[j]
        if t==last:
            last='o'
            continue
        if t=='p':
            score+=S
        elif t=='s':
            score+=R
        elif t=='r':
            score+=P
        last=t
print(score)
