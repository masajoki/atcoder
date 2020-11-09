N=int(input())
S=[]
for _ in range(N):
    s=list(input())
    s.reverse()
    S.append(s)
S.sort()

for s in S:
    s.reverse()
    t=''.join(s)
    print(t)
