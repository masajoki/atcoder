import copy
n,k=map(int,input().split())
a=list(map(int,input().split()))
maxed={}
for m in range(0,k):
    temp=[0]*n
    if len(maxed)==n:
        print(' '.join(map(str,a)))
        exit()
    for i in range(0,n):
        d=a[i]
        if d==n:
            temp[i]=n
            maxed[i]=1
        elif d !=0 :
            for x in range(i-d, i+d+1):
                if x >= 0 and x < n :
                    temp[x]+=1
        else:
            temp[i]+=1
    a=copy.copy(temp)

print(' '.join(map(str,a)))
