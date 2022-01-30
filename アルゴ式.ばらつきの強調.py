#アルゴ式.ばらつきの強調.py
import numpy
from statistics import mean
N,K=map(int,input().split())
H=list(map(int,input().split()))
A=numpy.array(H)



AD=0
AM=mean(A)
def bunsan(average,alist):
    ret=0
    for a in alist:
        ret+=(average-a)**2
    return ret/len(alist)

AD=bunsan(AM,A)
HD=bunsan(AM*K,A*K)

print(HD/AD)