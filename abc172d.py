def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort()
    return divisors
def divisors_count(n):
    divisors =0
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors+=1
            if i != n // i:
                divisors+=1
    return divisors

import math
def num_divisors_trial_division(n):
    num = 0
    for i in range(1, int(math.sqrt(n) + 1e-9) + 1):
        if n % i == 0:
            num += 1
            if n != i**2:
                num += 1
    
    return num

N=int(input())
answer=0

for i in range(1,N+1):
    k=num_divisors_trial_division(i)
    answer+=(i*k)

print(answer)