#063 - Monochromatic Subgrid（★4）
H,W=map(int,input().split())
P=[]
for i in range(H):
    p=list(map(int,input().split()))
    P.append(p)


ans=0
counter=[0 for _ in range(H*W+10)]
for i in range(2**H):
    counter={}
    for w in range(W):
        last=-1
        temp=0
        for j in range(H):
            if i & (1 << j):
                if last==-1:
                    temp+=1
                    last=P[j][w]
                elif last == P[j][w]:
                    temp+=1
                else:
                    last=-1
                    temp=0
                    break

        if last in counter.keys():
            counter[last]+=temp
        else:
            counter[last]=temp
    ans=max(ans,max(counter.values()))
print(ans)
