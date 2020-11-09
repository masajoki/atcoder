#Nのイワシ
#i匹目のイワシ：美味しさ〜Ai、香り〜Bi
#1匹以上のイワシを同じクーラーボックス
#共食いする２匹は同じにはできない
#Ai*Aj+Bi*Bj=0の時、一緒にできない
#イワシの選び方は何通りあるか。 
# 1000000007 で割ったあまりを出力する。

#1<=N<=200,000

#A*B のパターンを計算する
#全部１匹ずつはOK: N通り
#Pパターンあるとして、パターンPi(1<i<P)の魚の数をNiとするなら、
#P匹取りだす場合：1*N1*N2*ni*...*NP
#P-1匹取り出す場合：

import itertools
N=int(input())
Iwashies=[]
answer=0
for i in range(N):
    Iwashies.append(input().split())
ABdict={}
for iwashi in Iwashies:
    temp=int(iwashi[0])*int(iwashi[1])
    if temp in ABdict:
        ABdict[temp]=ABdict[temp]+1
    else:
        ABdict[temp]=1
for n in range(1,len(ABdict)+1):
    combis=itertools.combinations(ABdict,n)
    for c in combis:
        temp=1
        for item_c in c:
            temp*=ABdict[item_c]
        answer+=temp
print(answer%1000000007)
