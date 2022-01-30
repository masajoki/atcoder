#アルゴ式.平均値をずらす.py
#numpyはpython使えない
import numpy
N=int(input())
A=list(map(int,input().split()))
array=numpy.array(A)
arrayavg=array.mean()

B=array-arrayavg
print(*B)