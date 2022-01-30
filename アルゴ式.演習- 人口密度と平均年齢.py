#アルゴ式.演習: 人口密度と平均年齢.py
N=47
import statistics
X=[]
S=[]
P=[]
Ag=[]
JM=[]
for i in range(N):
    x,s,p,a=input().split()
    X.append(x)
    S.append(int(s))
    P.append(int(p))
    Ag.append(float(a))
    JM.append(int(p)/int(s))


#アルゴ式.データ間の関係性 2-2 (相関係数).py

A=JM
B=Ag
Amean=statistics.mean(A)
Bmean=statistics.mean(B)
Astdev=statistics.pstdev(A)
Bstdev=statistics.pstdev(B)
kyobunsan=0

for i in range(N):
    t1=Amean-A[i]
    t2=Bmean-B[i]
    kyobunsan+=t1*t2/N

r=kyobunsan/Astdev/Bstdev
print(r)