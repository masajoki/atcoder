A,B,K=map(int,input().split())
k=0
for i in range(min(A,B),0,-1):
    if A%i==0 and B%i==0:
        k+=1
        if k==K:
            print(i)
            exit()
