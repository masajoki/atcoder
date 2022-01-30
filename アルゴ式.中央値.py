#アルゴ式.中央値.py
N=int(input())
A=list(map(int,input().split()))
A.sort()
if N%2==0:
    print((A[N//2]+A[(N//2)-1])/2)
else:
    print(A[N//2])