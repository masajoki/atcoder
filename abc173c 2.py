#C H and V
import copy
H,W,K=map(int,input().split())
C=[]

for i in range(H):
    c=[]
    c=list(input())
    C.append(c)

ans=0
# tempC=C
for bitmaph in range(2**H):
    for bitmapw in range(2**W):
        tempC=copy.deepcopy(C)

        for i in range(H):
            bith= (bitmaph >> i & 1)
            if bith==1:
                for jt in range(W):
                    tempC[i][jt]="R"
        for j in range(W):
            bitw= (bitmapw >> j & 1)
            if bitw==1:
                for it in range(H):
                    tempC[it][j]="R"
        count=0
        for c in tempC:
            for a in c:
                if a == "#":
                    count+=1
        if count==K:
            ans+=1
print(ans)




