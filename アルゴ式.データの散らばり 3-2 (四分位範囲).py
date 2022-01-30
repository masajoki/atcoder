#アルゴ式.データの散らばり 3-2 (四分位範囲).py
import statistics
N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
A.sort()
B.sort()

def calc(A):
    amedian=statistics.median(A)
    if len(A)%2==0:
        return abs(statistics.median(A[:N//2])-statistics.median(A[N//2:]))
    else:
        return abs(statistics.median(A[:N//2])-statistics.median(A[N//2+1:]))

dA=calc(A)
dB=calc(B)

if dA==dB:
    print("same")
elif dA<dB:
    print("A")
else:
    print("B")