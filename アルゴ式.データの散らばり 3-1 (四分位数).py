#アルゴ式.データの散らばり 3-1 (四分位数).py
import statistics
N=int(input())
A=list(map(int,input().split()))
A.sort()
amedian=statistics.median(A)
if N%2==0:
    print(statistics.median(A[:N//2]),amedian,statistics.median(A[N//2:]))
else:
    print(statistics.median(A[:N//2]),amedian,statistics.median(A[N//2+1:]))