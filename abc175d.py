N,K=map(int,input().split())
P=list(map(int,input().split() ))
C=list(map(int,input().split() ))
score=0
maxscore=0
current=0
for _ in range(K):
    current=P[current]-1
    score+=C[current]
    if maxscore < score:
        maxscore=score

for _ in range(K,N):
    current=P[current]-1
    prev=P[current-K]-1
    score+=C[current]
    score-=C[prev]
    if maxscore < score:
        maxscore=score

print(maxscore)

