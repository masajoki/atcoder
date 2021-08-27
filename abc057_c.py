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

N=int(input())
divs=make_divisors(N)
ans=10
for d in divs:
    e=str(N//d)
    temp=max(len(e),len(str(d)))
    ans=min(ans,temp)
print(ans)
