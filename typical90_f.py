#a-zしかないので、ちょっとだけ凝った貪欲法で解ける

from collections import deque
import string
N,K=map(int,input().split())
S=input()
Q=deque()
Ans=[]
Count={}

#a-zの辞書を用意
for a in (list(string.ascii_lowercase)):
    Count[a]=deque()

#a-zの出現箇所を記録
for i in range(N):
    c=Count[S[i]]
    c.append(i)

last=-1
for i in range(K):
    for a in (list(string.ascii_lowercase)):
        if len(Ans)-1==i:
            break
        while len(Count[a])>0:
            t=Count[a].popleft()
            if t<=last: #前回利用した文字の位置以前の文字は利用しない
                continue
            elif last<t<=N-K+i:
                Ans.append(S[t])
                last=t
                break
            else:
                Count[a].appendleft(t)
                break
ans="".join(Ans)
print(ans)