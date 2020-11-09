N,M,Q=map(int,input().split())
s=[]
answered=[[] for _ in range(N+1)]
remain=[N]*(M+1)
queries=[]

for i in range(Q):
    queries.append(list(map(int,input().split())))

for q in queries:
    if q[0]==1:
        score=0
        for a in answered[q[1]]:
            score+=remain[a]
        print(score)

    elif q[0]==2:
        answered[q[1]].append(q[2])
        remain[q[2]]-=1


