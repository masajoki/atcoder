H,W=map(int,input().split())
S=[]
for i in range(H):
    S.append(input())

for i in range(H-1):
    for j in range(W-1):
        if S[i][j]=='#':
            temp=[]
            for k in (i-1,i+1):
                if 0<=k<H:
                    temp.append(S[k][j])
            for m in (j-1,j+1):
                if 0<=m<W:
                    temp.append(S[i][m])
            if '#' not in temp:
                print("No")
                exit()

print("Yes")

