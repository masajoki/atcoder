import bisect
import array

# from collections import deque

def main():
    L,Q=map(int,input().split())
    C=array.array('i',[0,L])
    query=[]
    for i in range(Q):
        c,x=map(int,input().split())
        query.append((c,x))

    for i in range(Q):
        c,x=query[i]

        if c==1:
            pos=bisect.insort(C,x)
        else:
            pos=bisect.bisect_right(C,x)
            ans=C[pos]-C[pos-1]
            print(ans)

main()