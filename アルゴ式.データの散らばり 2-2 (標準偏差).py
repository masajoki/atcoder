#データの散らばり 2-2 (標準偏差).py
#アルゴ式.データの散らばり 2-1 (分散).py
import statistics
N=int(input())
A=list(map(int,input().split()))

AD=0
AM=statistics.mean(A)
def bunsan(average,alist):
    ret=0
    for a in alist:
        ret+=(average-a)**2

    return ret/N

AD=bunsan(AM,A)
print(AD)
print(AD**0.5)

# stddevは標本標準偏差でpstdevとはことなる
# print(statistics.pstdev(A))