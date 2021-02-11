N,Wlimit=map(int,input().split())
V=[]
W=[]
for i in range(N):
    v,w=map(int,input().split())
    V.append(v)
    W.append(w)

# 1<=N<=200
# 1<=Wlimit<=1000000007)

maxans=0
if N<=28:
    for i in range(2**N):
        v=0
        w=0        
        for b in range(N):
            if i>>b&1==1:
                v+=V[b]       
                w+=W[b]
        if w <= Wlimit:
            maxans=max(v,maxans)
    print(maxans)
