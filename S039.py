H,W=map(int,input().split())
S=[]
Sp=[[W for _ in range(W)] for _ in range(H)]
for i in range(H):
    s=input()
    S.append(s)
    lastpos=-1
    for j in range(W-1,-1,-1):
        if s[j]=='#':
            lastpos=j
        if lastpos!=-1:
            Sp[i][j]=lastpos


maxarea=0
broken=False
for i in range(H):
    for j in range(W):
        for w in range(W-j):
            area=0
            for h in range(H-i):
                if Sp[i+h][j]>j+w:
                    area+=(w+1)  
                else:
                    maxarea=max(maxarea,area)
                    break
            maxarea=max(maxarea,area)
print(maxarea)