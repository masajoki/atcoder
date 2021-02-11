import sys
import  copy
sys.setrecursionlimit(10**7) 

def main():
    from builtins import input, int, map
    def bfs(nowTown,startTown,cost,visitedcost):
        for t in Path[nowTown]:
            newCost=cost+Cost[nowTown][t]
            if newCost >= dp[startTown]:
                continue
            if t == startTown and dp[startTown]>newCost:
                dp[startTown]=newCost
            elif visitedcost[t]>newCost:
                visitedcost[t]=newCost
                bfs(t,startTown,newCost,visitedcost)

    N,M=map(int,input().split())
    A=set()
    Cost=[[10**5+1 for _ in range(N+10)] for _ in range(N+10)]
    Path=[[] for _ in range(N+10)]
    for i in range(M):
        a,b,c=map(int,sys.stdin.readline().split())
        A.add(a)
        if Cost[a][b]>c:
            Cost[a][b]=c
            Path[a].append(b)
    dp=[999999999 for _ in range(N+10)]
    visitedcost=[999999999 for _ in range(N+10)]

    for a in A:
        visitedcost=[999999999 for _ in range(N+10)]
        bfs(a,a,0,visitedcost)

    for i in range(1,N+1):
        if dp[i]== 999999999:
            print(-1)
        else:
            print(dp[i])

main()