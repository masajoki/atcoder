#abc237_e.py
# from collections import deque
def main():
    import heapq
    import sys
    input=sys.stdin.readline

    N,M=map(int,input().split())
    H=list(map(int,input().split()))
    Cost={}
    E=[[] for _ in range(N+1)]
    for i in range(M):
        ut,vt=map(int,input().split())
        u=ut-1
        v=vt-1
        E[u].append(v)
        E[v].append(u)
        hu=H[u]
        hv=H[v]
        uvdiff=hu-hv
        vudiff=hv-hu
        if hu==hv:
            Cost[(u,v)]=0
            Cost[(v,u)]=0
        elif hu>hv:
            Cost[(u,v)]=0
            Cost[(v,u)]=uvdiff
        else:
            Cost[(v,u)]=0
            Cost[(u,v)]=vudiff

    queue=[]
    #ダイクストラ
    INF=10**10
    dp=[INF for _ in range(N+1)]
    dp[0]=0
    heapq.heappush(queue,(0,0))
    while queue:
        cost,vertex=heapq.heappop(queue)
        if dp[vertex]<cost:
            continue

        for nv in E[vertex]:
            if dp[nv]>cost+Cost[vertex,nv]:
                dp[nv]=cost+Cost[vertex,nv]
                heapq.heappush(queue,(dp[nv],nv))

#スタート地点からの高度差を反映する
    for i in range(N):
        dp[i]+=H[i]-H[0]

    print(-1*min(dp))

main()