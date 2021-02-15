A=[]
max=9
digits=5

def dfs(start):
    if len(A)==digits:
        print("".join(A))
    for i in range(start,max+1):
        A.append(str(i))
        dfs(i)
        A.pop
    
dfs(1)