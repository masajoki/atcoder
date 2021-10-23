import heapq
M=[]
N=int(input())
P=[]
for i in range(N):
    m=list(map(int,input().split()))
    M.append(m)

for i in range(N):
    for j in range(N):


        if 0<=i-1:
            if M[i][j]>M[i-1][j] :
                pass
            else:
                continue
        if i+1<N:
            if M[i][j]>M[i+1][j] :
                pass
            else:
                continue
        if 0<=j-1:
            if M[i][j]>M[i][j-1] :
                pass
            else:
                continue
        if j+1<N:
            if M[i][j]>M[i][j+1]:    
                pass
            else:
                continue

        heapq.heappush(P,-M[i][j])

for i in P:
    print(-i)
