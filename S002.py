from collections import deque
W,H=map(int,input().split())
Q=deque()
M=[]
S=[-1,-1]
visited=[[0 for _ in range(W)] for _ in range(H)]
for i in range(H):
    m=list(input().split())
    M.append(m)
    if "s" in m:
        w=m.index("s")
        S=[i,w]

Q.append((S[0],S[1],0))

visited[S[0]][S[1]]=1

while len(Q)>0:
    hp,wp,l=Q.popleft()
    if M[hp][wp]=='g':
        print(l)
        exit()
    for h,w in [(1,0),(-1,0),(0,1),(0,-1)]:
        if 0<=(h+hp)<H and 0<=(w+wp)<W:
            if visited[h+hp][w+wp]==0 and M[h+hp][w+wp]!='1':
                Q.append((h+hp,w+wp,l+1))
                visited[h+hp][w+wp]=1


print("Fail")


