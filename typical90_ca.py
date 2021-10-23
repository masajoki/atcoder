# 079 - Two by Two（★3） 
H,W=map(int,input().split())
A=[]
B=[]

for i in range(H):
    a=list(map(int,input().split()))
    A.append(a)

for i in range(H):
    a=list(map(int,input().split()))
    B.append(a)

ans=0
for i in range(H-1):
    for j in range(W-1):
        temp=B[i][j]-A[i][j]
        ans+=abs(temp)
        A[i][j]+=temp
        A[i][j+1]+=temp
        A[i+1][j]+=temp
        A[i+1][j+1]+=temp

for i in range(H):
    if A[i][W-1]!=B[i][W-1]:
            print("No")
            exit()

for j in range(W):
    if A[H-1][j]!=B[H-1][j]:
            print("No")
            exit()

print("Yes")
print(ans)