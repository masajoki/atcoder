n=int(input())
memo=[-1 for _ in range(n+1)]
def fibo(n):
    # fibonacci数列を求める練習
    # Fn=Fn-1+Fn-2
    # F0=0
    # F1=1
    print("fibo("+str(n)+"), ",end=" ")
    #ベースケース
    if n in (0,1):
        print("ベースケース:"+str(n))
        return n
    
    if memo[n]!=-1:
        print("memo化利用:"+str(n))
        return memo[n]
    else:
        print("再帰呼び出し for:"+str(n-1)+","+str(n-2))
        memo[n]=fibo(n-1)+fibo(n-2)    
        return memo[n]

print(fibo(n))