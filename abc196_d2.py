#解説見ての実装
import copy
H,W,A,B=map(int,input().split())
ans=0
def dfs(h,w,calledplaced, countA,countB):
    global ans

    if calledplaced[h][w]==0 and h<H-1 and calledplaced[h+1][w]==0 and countA<A:
        placed=copy.deepcopy(calledplaced)
        # print("縦-------")
        # print(countA,countB,placed)
        placed[h][w]=1
        placed[h+1][w]=1
        # print(countA+1,countB,placed)
        # print("-------")
        if countA+1==A and countB==B:
            # print("ans")
            ans+=1
        else:
            if w+1<=W-1:
                dfs(h,w+1,placed,countA+1,countB)
            elif h+1<=H-1:
                dfs(h+1,0,placed,countA+1,countB)

    if calledplaced[h][w]==0 and w<W-1 and calledplaced[h][w+1]==0 and countA<A:
        placed=copy.deepcopy(calledplaced)
        # print("横-------")
        # print(countA,countB,placed)
        placed[h][w]=1
        placed[h][w+1]=1
        # print(countA+1,countB,placed)
        # print("-------")

        if countA+1==A and countB==B:
            # print("ans")
            ans+=1
        else:
            if w+1<=W-1:
                dfs(h,w+1,placed,countA+1,countB)
            elif h+1<=H-1:
                dfs(h+1,0,placed,countA+1,countB)


    placed=copy.deepcopy(calledplaced)
    if calledplaced[h][w]==0 and countB<B:
        # print("単-------")
        # print(countA,countB,placed)
        placed[h][w]=1
        countB+=1
        # print(countA,countB,placed)
        # print("-------")
        if countA==A and countB==B:
            # print("ans")
            ans+=1
            return

    if w+1<=W-1:
        dfs(h,w+1,placed,countA,countB)
    elif h+1<=H-1:
        dfs(h+1,0,placed,countA,countB)

placed=[[0 for _ in range(W) ]for _ in range(H)]

dfs(0,0,placed,0,0)
print(ans)
