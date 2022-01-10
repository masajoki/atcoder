#typical90_cg
#085 - Multiplication 085（★4）
# 問題文
# 正の整数 K が与えられます。abc=K を満たす正の整数 (a,b,c) (a≤b≤c) の組がいくつあるかを求めてください。
# 制約 1≤K≤10**12
# from collections import defaultdict
# from itertools import product
K=int(input())

#1を含む約数を全て返す
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

divisors=make_divisors(K)
ans=0


#約数の組み合わせを考える
for d in divisors:
        tK=K//d
        if tK < d:
            break
        for e in divisors:
            if e < d:
                continue
            elif tK %e ==0 and e <= tK //e :
                ans+=1
            elif e > tK //e :
                break
print(ans)
        
