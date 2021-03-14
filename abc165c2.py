#深さ優先探索怖くない
N,M,Q=map(int,input().split())
A=[]
B=[]
C=[]
D=[]
for i in range(Q):
    a,b,c,d=map(int,input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

S=[]
start=1
digit=N
ans=0

def calc():
    temp=0
    global ans
    for i in range(Q):
        if (S[B[i]-1]-S[A[i]-1])==C[i]:
            temp+=D[i]
    # if temp >= ans:
        # print(temp, S)
    ans=max(temp,ans)

def dfs(start):
    if len(S)==digit:
        calc()
        return
    for i in range(start,M+1):
        S.append(i)
        dfs(i)
        S.pop()
        
dfs(start)
print(ans)
