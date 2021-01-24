#初歩的な動的計画法

N=int(input())
def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]

if (N<2):
    print(-1)
    exit()

P=primes(N)
dp=[[-1 for _ in range(N+1)] for _ in range(len(P))]
dp[0][0]=0
dp[0][P[0]]=1
for i in range(len(P)-1):
    for j in range(N+1):
        if j-P[i+1]>=0 and dp[i][j-P[i+1]]>=0:
            dp[i+1][j]=max(dp[i][j-P[i+1]]+1,dp[i][j])
        else:
            dp[i+1][j]=dp[i][j]
print(dp[len(P)-1][N])
