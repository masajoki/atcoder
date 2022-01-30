import statistics
import numpy
N=int(input())
H=list(map(int,input().split()))

hmean=statistics.mean(H)
hstddev=statistics.pstdev(H)
Harray=numpy.array(H)
T=Harray-hmean
T=T/hstddev
print(*T)