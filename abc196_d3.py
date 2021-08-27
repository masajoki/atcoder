#解説見ての実装
import copy
H,W,A,B=map(int,input().split())
ans=0
def dfs(h,w,calledplaced, cntA,cntB):
    global ans
    if cntA==A and cntB==B and h==H-1 and w==W-1:
        ans+=1
        return

    if calledplaced[h][w]==0 and h<H-1 and calledplaced[h+1][w]==0 and cntA<A:
        placed=copy.deepcopy(calledplaced)
        placed[h][w]=1
        placed[h+1][w]=1
        if w+1<=W-1:
            dfs(h,w+1,placed,cntA+1,cntB)
        elif h+1<=H-1:
            dfs(h+1,0,placed,cntA+1,cntB)

    if calledplaced[h][w]==0 and w<W-1 and calledplaced[h][w+1]==0 and cntA<A:
        placed=copy.deepcopy(calledplaced)
        placed[h][w]=1
        placed[h][w+1]=1
        if w+1<=W-1:
            dfs(h,w+1,placed,cntA+1,cntB)
        elif h+1<=H-1:
            dfs(h+1,0,placed,cntA+1,cntB)


    placed=copy.deepcopy(calledplaced)
    if calledplaced[h][w]==0 and cntB<B:
        placed[h][w]=1
        cntB+=1

    if w+1<=W-1:
        dfs(h,w+1,placed,cntA,cntB)
    elif h+1<=H-1:
        dfs(h+1,0,placed,cntA,cntB)

placed=[[0 for _ in range(W) ]for _ in range(H)]

dfs(0,0,placed,0,0)
print(ans)
