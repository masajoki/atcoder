A=[[ 0 for _ in range(3)] for _ in range(3)]
for i in range(3):
    A[i]=list(map(int,input().split()))

N=int(input())
B=[]
for _ in range(N):
    B.append(int(input()))

for b in B:
    for a in A:
        if b in a:
            a[a.index(b)]=0

for i in range(3):
    if A[i][0]== 0 and A[i][1]== 0 and A[i][2]== 0 :
        print('Yes')
        exit()
    if A[0][i]== 0 and A[1][i]== 0 and A[2][i]== 0 :
        print('Yes')
        exit()
    if A[0][0] ==0 and A[1][1] ==0 and A[2][2] ==0:
        print('Yes')
        exit()
    if A[0][2] ==0 and A[1][1] ==0 and A[2][0] ==0:
        print('Yes')
        exit()
print("No")