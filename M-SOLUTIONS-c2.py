"""
1  年間の課程を 
N 個の学期に分割

1  学期から K−1 学期までの評点：付けられない

K  学期から N 学期までの評点：その学期を含めた直近 K 回の期末テストの点数を掛け算したもの。
"""
N,K=map(int,input().split())
A=list(map(int,input().split()))
hyouten=[0]*(N+5)

hyouten[K-1]=A[0]
for i in range(1,K):
    hyouten[K-1]*=A[i]

for i in range(K,N):
    hyouten[i]=hyouten[i-1]*A[i]/A[i-K]

for i in range(K,N):

    if hyouten[i] > hyouten[i-1]:
        # print(hyouten[i-1],hyouten[i])
        print("Yes")
    else:
        # print(hyouten[i-1],hyouten[i])
        print("No")
    
