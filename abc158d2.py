#普通のリストとかストリング連結使うと遅いから、両側から追加してもO(1)で処理できるdequeを利用する

import collections
St=list(input())
S=collections.deque(St)
# for s in St:
#     S.append(s)

Q=int(input())
reversed=False
for i in range(Q):
    q=list(input().split())
    if q[0]=='1':
        reversed= not(reversed)
    else:
        if q[1]=='1':
            if reversed:
                S.append(q[2])
            else:
                S.appendleft(q[2])
        else:
            if reversed:
                S.appendleft(q[2])
            else:
                S.append(q[2])

if reversed:
    S.reverse()
print(''.join(S))
