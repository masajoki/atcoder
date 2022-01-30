#アルゴ式.平均値をずらしたデータの分散.py

import numpy
from statistics import mean
N=int(input())
A=list(map(int,input().split()))
array=numpy.array(A)
arrayavg=array.mean()
B=array-arrayavg


AD=0
BD=0
AM=mean(A)
BM=mean(B)
def bunsan(average,alist):
    ret=0
    for a in alist:
        ret+=(average-a)**2

    return ret/len(alist)

AD=bunsan(AM,A)
BD=bunsan(BM,B)

print(BD/AD)