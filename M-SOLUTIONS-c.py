"""
1  年間の課程を 
N 個の学期に分割

1  学期から K−1 学期までの評点：付けられない

K  学期から N 学期までの評点：その学期を含めた直近 K 回の期末テストの点数を掛け算したもの。
"""
N,K=map(int,input().split())
A=list(map(int,input().split()))
hyouten=[0]*(N+5)

for i in range(K+1,N+1):
    for j in range(i-K,i):
        if hyouten[i]==0:
            hyouten[i]=A[j]
        else:
            hyouten[i]*=A[j]
    prevhyouten=hyouten[i]/A[i-1]*A[i-K-1]
    if hyouten[i] > prevhyouten:
        # print(prevhyouten,hyouten[i])
        print("Yes")
    else:
        # print(prevhyouten,hyouten[i])
        print("No")
    
