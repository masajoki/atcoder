N,M=map(int,input().split())
S=[]
C=[]
        
for i in range(M):
    s,c=map(int,input().split())
    S.append(s)
    C.append(c)

ck=[ [] for _ in range(N)]
for i in range(M):

    if len(ck[S[i]-1])>0 and C[i] not in ck[S[i]-1]:
        print(-1) 
        exit()
    else:
        ck[S[i]-1].append(C[i])

if N==1:
    ans=[0]
else:
    ans=[1]
for i in range(1,N):
    ans.append(0)

for i in range(M):
    ans[S[i]-1]=C[i]



if N==1:
    print(ans[0])    
elif ans[0]==0:
    print(-1)
else:
    for i in ans:
        print(i,end='')
    print("")
