#D floor function
A,B,N=map(int,input().split())

#N以下の非負整数xに対するfloor(Ax/b)-Axflor(x/B)の最大値を整数として出力

# A <= 10**6
# B <= 10**12
# N <= 10**12

for x in range(N+1):
    ans=(A-A%B)*(x%B)/B
    print(x,ans)