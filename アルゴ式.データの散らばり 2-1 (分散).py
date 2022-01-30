#アルゴ式.データの散らばり 2-1 (分散).py
from statistics import mean
N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

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

if AD==BD:
    print("same")
elif AD>BD:
    print("B")
else:
    print("A")