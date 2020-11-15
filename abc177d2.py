    from collections import deque
    N,M=map(int,input().split())
    Pairs=[]
    Friends=[ set() for _ in range(N)]

    for i in range(M):
        a,b=map(int,input().split())
        Pairs.append([a-1,b-1])
        Friends[a-1].add(b-1)
        Friends[b-1].add(a-1)

    FriendGroup=[ 0 for _ in range(N)] #FriendGroupIDを1~

    queue=deque()

    friendgrp=1
    for i in range(N):
        if FriendGroup[i]==0:
            queue.append(Friends[i])
        while queue:
            pair=queue.popleft() 
            for p in pair:
                if FriendGroup[p]!=friendgrp:
                    FriendGroup[p]=friendgrp
                    queue.append(Friends[p])
        friendgrp+=1


    groupsize=[ 0 for _ in range(friendgrp+1)]
    for g in FriendGroup:
        if g!=0:
            groupsize[g]+=1

    print(max(1,max(groupsize)))
