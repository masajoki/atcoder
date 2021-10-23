N,X=map(int,input().split())
A=list(map(int,input().split()))
#メモ化再帰はDPと同じなんだな
#でも明確にループがある分、
memo=[[False for _ in range(X+1)] for _ in range(N+1)]
def func(i,j):
    global memo
    memo[i][j]=True
    if i==0:
        if j==0:
            return True
        else:
            return False
    else:
        if j>=A[i-1]:
            if memo[i-1][j-A[i-1]]==False:
                func(i-1,j-A[i-1])
        if memo[i-1][j]==False:
            func(i-1,j)
                
func(N,X)
if memo[0][0]==True:
    print("Yes")
else:
    print("No")
