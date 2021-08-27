N=int(input())
H=list(map(int,input().split()))

nonzerocount=0
while H.count(0)!=len(H):
    last=-1
    for i in range(len(H)):
        h=H[i]
        if h>0 and (last==0 or last==-1):
            nonzerocount+=1
        last=h
        if h!=0:
            H[i]-=1
print(nonzerocount)






