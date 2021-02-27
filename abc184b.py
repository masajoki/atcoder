n,x=map(int,input().split())
S=list(input())
score=x
for s in S:
    if s=='x':
        score=max(score-1,0)
    else:
        score+=1
print(score)