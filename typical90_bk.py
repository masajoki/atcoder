#063 - Monochromatic Subgrid（★4）
H,W=map(int,input().split())
P=[]
for i in range(H):
    p=list(map(int,input().split()))
    P.append(p)


counter={}
for i in range(2**H):
    for j in range(H):
        if i & (1 << j):
            for w in range(W):
                if 

