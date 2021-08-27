H,W=map(int,input().split())
A=[]
path=0
for _ in range(H):
    a=input()
    A.append(a)
    path+=a.count('#')


def bfs(h,w):
    if h==H-1 and w==W-1:
        return True
    for y,x in ((h+1,w),(h,w+1)):
        if y<H and x<W and A[y][x]=='#':
            return bfs(y,x)
    

if bfs(0,0)==True :
    if  path==H+W-1:
        print("Possible")
    else:
        print("Impossible")
else:
    print("Impossible")