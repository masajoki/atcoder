# AtCoder Beginner Contest 168D
from collections import deque

#頂点の数と辺の数。mapは入力を一括して
N,M=map(int,input().split())

#辺
# for _ in range(M)で、M個のA-Bリストを作ってる。
AB=[map(int,input().split()) for _ in range(M)]

#無向リスト, path[origin][target1, target2, ...]  を作る
path=[ [] for _ in range(N+1)]
for a,b in AB: #両向きにする
    path[a].append(b)
    path[b].append(a)

#最終的に返す標識一覧. -1は標識がない
# sign[部屋番号]=宛先部屋番号
sign = [-1]*(N+1)

#部屋番号１から初めて次に訪問するキュー.初期値として１を入れておく。
visitque=deque([1])

while visitque:
    queued_room = visitque.popleft()
    for linked_room_from_queued_room in path[queued_room]:
        if sign[linked_room_from_queued_room]==-1:
            sign[linked_room_from_queued_room]=queued_room #
            visitque.append(linked_room_from_queued_room)

print('Yes')
print('\n'.join(str(v) for v in sign[2:]))



