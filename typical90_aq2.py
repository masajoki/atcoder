from collections import deque

direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

H, W = map(int, input().split())
sr, sc = map(int, input().split()) #スタート地点(sr,sc)
sr -= 1 #0オリジンに変更してる
sc -= 1
gr, gc = map(int, input().split()) #ゴール地点(gr,gc)
gr -= 1
gc -= 1
S = [list(input()) for _ in range(H)]

INF = float('inf')
dp = [[INF for _ in range(W)] for _ in range(H)]
dp[sr][sc] = 0
queue = deque([(0, sr, sc, -1)]) #cnt, cr, cc, cdir 
while queue:
    cnt, cr, cc, cdir = queue.popleft() #cr,cc は現在の行と列番号。cntはなんだろう？ cdir は現在の向きのリスト番号
    if cnt > dp[cr][cc]:
        continue
    if cr == gr and cc == gc: # ゴールに到達したらそこで中断している
        print(cnt)
        break
    for ndir in range(4): 
        nr = cr + direction[ndir][0] #nr: next row
        nc = cc + direction[ndir][1] #nc: next column
        if nr < 0 or nr >= H or nc < 0 or nc >= W: #枠外ならcontinue
            continue
        if S[nr][nc] == '#': #壁ならcontinue
            continue
        dir_diff = ndir - cdir 
        if dir_diff == 0:
            ncnt = cnt
        else:
            if cdir == -1:
                ncnt = cnt
            else:
                ncnt = cnt + 1
        if ncnt > dp[nr][nc]:
            continue
        dp[nr][nc] = ncnt
        if ncnt == cnt:
            queue.appendleft((ncnt, nr, nc, ndir)) #同じコストで行けるところを先に潰す
        else:
            queue.append((ncnt, nr, nc, ndir))

