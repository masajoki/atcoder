H,W=map(int,input().split())
S=[]
for i in range(H):
    s=input()
    S.append(s)


Reds=[ '' for _ in range(H+W+2)]

for i in range(H): 
    for j in range(W):
        if S[i][j]=='R' and Reds[i+j] in ('',"R"):
            Reds[i+j]="R"
        elif S[i][j]=='B'and Reds[i+j] in ('','B'):
            Reds[i+j]='B'
        elif S[i][j]=='R' and Reds[i+j] =='B':
            print(0)
            exit()
        elif S[i][j]=='B' and Reds[i+j] =='R':
            print(0)
            exit()

ans=1
for i in range(W+H-1):
    if Reds[i]=='':
        ans*=2
        ans=ans%998244353

print(ans)