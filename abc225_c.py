N,M=map(int,input().split())
B=[]
for i in range(N):
    b=list(map(int,input().split()))
    for i in range(M-1):
        if b[i+1]-b[i]!=1:
            print("No")
            exit()
        elif  b[i]%7==0:
            print("No")
            exit()

    B.append(b)
    if len(B)==1:
        continue
    for i in range(M):
        if B[len(B)-1][i]-B[len(B)-2][i]!=7:
            print("No")
            exit()
print("Yes")
        

