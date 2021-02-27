H, W = map(int, input().split())
S = []
ans = [[0 for _ in range(W)] for _ in range(H)]
for i in range(H):
    S.append(input())

def countbomb(y, x):
    count = 0
    for a in (-1, 0, 1):
        for b in (-1, 0, 1):
            if a == 0 and b == 0:
                continue
            h = y + a
            w = x + b
            if 0 <= h < H and 0 <= w < W:
                if S[h][w] == "#":
                    count += 1
    return count

for h in range(H):
    for w in range(W):
        if S[h][w] == '.':
            ans[h][w] = str(countbomb(h, w))
        else:
            ans[h][w] = "#"
    print(''.join(ans[h]))
