from collections import defaultdict
n, q = map(int, input().split())
e = defaultdict(list)
for i in range(n-1):
    a, b = map(int, input().split())
    e[a-1].append(b-1)
    e[b-1].append(a-1)
counter = [0] * n
for j in range(q):
    p, x = map(int, input().split())
    counter[p-1] += x
stack = [0]
visited = [False] * n
while stack:
    parent = stack.pop()
    visited[parent] = True
    for child in e[parent]:
        if visited[child]:
            continue
        counter[child] += counter[parent]
        stack.append(child)
print(*counter)