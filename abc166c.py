N,M=map(int,input().split())
peaks=list(map(int,input().split()))
goodpeaks=[1]*N
for i in range(M):
    a,b=map(int,input().split())
    if peaks[a-1]<peaks[b-1]:
        goodpeaks[a-1]=0
    elif peaks[a-1]>peaks[b-1]:
        goodpeaks[b-1]=0
    elif peaks[a-1]==peaks[b-1]:
        goodpeaks[a-1]=0
        goodpeaks[b-1]=0
#    print(goodpeaks)
ans=0
for h in goodpeaks:
    if h != 0:
        ans+=1

print(ans)