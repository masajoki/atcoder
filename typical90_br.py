#070 - Plant Planning（★4） 
#https://atcoder.jp/contests/typical90/tasks/typical90_br
# 
# 二次元平面上に N 棟の工場があり
# これからあなたは二次元平面上の好きな場所を 1 つ選び、発電所を建設します。
# 発電所の不便さを、発電所から各工場までのマンハッタン距離の総和と定義するとき、
# #不便さとしてありうる最小の値を求めてください。なお、この問題の制約下で答えは整数となることが証明できます。

# 答え見てAC
# 中央値が最小となる

N=int(input())
X=[]
Y=[]

def calcX(val):
    distance=0
    for x in X:
        distance+=abs(x-val)
    return distance

def calcY(val):
    distance=0
    for y in Y:
        distance+=abs(y-val)
    return distance

for i in range(N):
    x,y=map(int,input().split())
    X.append(x)
    Y.append(y)

X.sort()
Y.sort()

print(calcX(X[N//2])+calcY(Y[N//2]))
