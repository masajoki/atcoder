N,M=map(int,input().split())
A=[]
B=[]
for i in range(N):
    A.append(input())

for i in range(M):
    B.append(input())

for i in range(N-M+1):
    for j in range(N-M+1):
        check=True
        for k in range(M):
            for m in range(M):
                if A[i+k][j+m]!=B[k][m]:
                    check=False
                    break
            if check==False:
                break
        if check:
            print("Yes")
            exit()
print("No")