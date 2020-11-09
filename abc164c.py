# くじ引きを 
# N
#  回行い、
# i
#  回目には種類が文字列 
# S
# i
#  で表される景品を手に入れました。

# 何種類の景品を手に入れましたか？

N=int(input())
S=set()
for _ in range(N):
    S.add(input())
print(len(S))