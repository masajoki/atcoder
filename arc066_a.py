N=int(input())
A=map(int,input().split())
count=[0 for _ in range(N+1)]

for a in A:
    count[a]+=1

for i in range(N+1):
    if N%2==0:
        if i%2==1 and count[i]==2:
            pass
        elif i%2 ==0 and count[i]==0:
            pass
        else:
            print("0")
            exit()
    else:
        if i==0 and count[i]==1:
            pass
        elif i%2==0 and count[i]==2:
            pass
        elif i%2==1 and count[i]==0:
            pass
        else:
            print("0")
            exit()
print(pow(2,N//2,10**9+7))
        