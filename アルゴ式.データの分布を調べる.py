#アルゴ式.データの分布を調べる.py
N=int(input())
A=list(map(int,input().split()))
X=[0]*5
for a in A:
    if a==0:
        X[0]+=1
    else:
        t=(a-1)//20
        X[t]+=1

for x in X:
    print(x)