N, K = map(int, input().split())
T = list(input())
for i in range(K, N):
    if T[i] == T[i-K]:
        T[i] = 'x'
print("".join(T))