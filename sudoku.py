A=[[] for _ in range(9)]
for i in range(9):
    s=list(map(int,list(input())))
    A[i]=s

def checkvert(i,j,n):
    for a in range(9):
        if A[a][j]==n:
            return False
    return True
    
def checkhori(i,j,n):
    for a in range(9):
        if A[i][a]==n:
            return False
    return True

def checkbox(i,j,n):
    yini=3*(i//3)
    xini=3*(j//3)
    for y in range(yini,yini+3):
        for x in range(xini,xini+3):
            if A[y][x]==n:
                return False
    return True

def check(i,j,n):
    if checkbox(i,j,n)  and  checkhori(i,j,n) and checkvert(i,j,n):
        return True
    else:
        return False

def solve(i,j):
    global A
    if j==0 and i==9:
        return True
    jnext=0
    inext=0

    if j==8:
        inext=i+1
        jnext=0
    else:
        inext=i
        jnext=j+1

    if A[i][j]!=0:
        return solve(inext,jnext)
    else:
        for n in range(1,10):
            if A[i][j]==0 and check(i,j,n)==True:
                # print("i:",i,"j:",j,"n:",n)
                A[i][j]=n
                result=solve(inext,jnext)
                if result==True:
                    return True 
                else:
                    A[i][j]=0
        return False
solve(0,0)

print("---------")
for i in range(9):
    
    print ("".join(map(str,A[i])))
exit()
