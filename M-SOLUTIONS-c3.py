"""
1  年間の課程を 
N 個の学期に分割

1  学期から K−1 学期までの評点：付けられない

K  学期から N 学期までの評点：その学期を含めた直近 K 回の期末テストの点数を掛け算したもの。
"""
N,K=map(int,input().split())
A=list(map(int,input().split()))
for i in range(0,N-K):
    if A[i]< A[i+K]:
        print("Yes")
    else:
        print("No")