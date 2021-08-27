N=int(input())
P=list(map(int,input().split()))

ans=0
i=0
if N==0:
    print(0)
    exit()
while i<N-1:
    if P[i]-1==i:
        if P[i+1]-1==i+1:
            t=P[i+1]
            P[i+1]=P[i]
            P[i]=t
            ans+=1
            i+=2
        else:
            t=P[i+1]
            P[i+1]=P[i]
            P[i]=t
            ans+=1
            i+=1
    else:
        i+=1
if P[N-1]==N:
    print(ans+1)
else:
    
    print(ans)