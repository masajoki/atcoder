from collections import deque

H, W = map(int, input().split())

start = list(map(int, input().split()))
dest = list(map(int, input().split()))
wall = '#'
road = '.'
inf = 999999999999
S = []
cost = [[inf for _ in range(W+1)] for _ in range(H+1)]

for i in range(H):
    S.append(list(input()))

queue = deque()

def chkBound(pos):
    h = pos[0]
    w = pos[1]
    if 0 < h <= H and 0 < w <= W and S[h-1][w-1] ==road:
        return True
    else:
        return False


def walk(pos):
    h = pos[0]
    w = pos[1]
    pathes = [[h-1, w], [h+1, w], [h, w+1], [h, w-1]]
    for p in pathes:
        if chkBound(p):
            h2 = p[0]
            w2 = p[1]
            if cost[h2][w2] > cost[h][w]:
                queue.appendleft(p)
                cost[h2][w2] = cost[h][w]

def magic(pos):
    h = pos[0]
    w = pos[1]
    pathes = []
    removepath=[[h-1, w], [h+1, w], [h, w+1], [h, w-1]]
    for i in [h-2, h-1, 0, h+1, h+2]:
        for j in [w-2, w-1, 0, w+1, w+2]:
            if chkBound([i,j]):
                if [i,j] not in removepath:
                    pathes.append([i, j])
    for p in pathes:
        h2 = p[0]
        w2 = p[1]
        if cost[h2][w2] > (cost[h][w] +1):
            queue.append(p)
            cost[h2][w2] = (cost[h][w] +1)


cost[start[0]][start[1]] = 0
queue.append(start)
while len(queue) > 0:
    pos = queue.popleft()
    if pos == dest:
        print(cost[pos[0]][pos[1]])
        exit()
    else:
        walk(pos)
        magic(pos)
print(-1)
