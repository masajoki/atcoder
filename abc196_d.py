import itertools 
H,W,A,B=map(int,input().split())

def check(strp):
    p=list(map(int,strp))
    placed=[[0 for _ in range(W) ]for _ in range(H)]
    for h in range(H):
        for w in range(W):
            pos=(W)*h+w
            if p[pos]==1:
                if placed[h][w]==0 and h<H-1 and placed[h+1][w]==0:
                    placed[h][w]=1
                    placed[h+1][w]=1
                else:
                    return False
            elif p[pos]==2:
                if placed[h][w]==0 and w<W-1 and placed[h][w+1]==0:
                    placed[h][w]=1
                    placed[h][w+1]=1
                else:
                    return False

    return True
ans=0

seeds=[]
seed=str(0)*(H*W-A)
for i in range(A+1):
    temp="1"*(i)+"2"*(A-i)
    seeds.append(seed+temp)


for seed in seeds:
    pattern = itertools.permutations(seed)
    patternlist=set(pattern)
    for p in patternlist:
        if H*W-p.count("0")!=A:
            continue
        else:
            if check(p):
                ans+=1


print(ans)