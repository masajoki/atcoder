N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()
i = 0
j = 0
while i < N and j < M:
    if A[i] == B[j]:
        print(A[i])
        i += 1
        j += 1
    elif A[i] < B[j]:
        i += 1
    elif A[i] > B[j]:
        j += 1
