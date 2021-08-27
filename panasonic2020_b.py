H,W=map(int,input().split())
if 1 in (H,W):
    print(1)
    exit()
if H%2==0:
    if W%2==0:
        ans=W//2*H
    else:
        ans=(W//2)*(H//2)+(W//2+1)*(H//2)
if H%2!=0:
    if W%2==0:
        ans=W//2*H
    else:
        ans=(W//2+1)*(H//2+1)+(W//2)*(H//2)
print(ans)
