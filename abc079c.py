S=input()
A=S[0]
B=S[1]
C=S[2]
D=S[3]

Z=[]
max=1
digits=3

def dfs(start):
    if len(Z)==digits:
        if int(A)+Z[0]*int(B)+Z[1]*int(C)+Z[2]*int(D) == 7:
            for i in range(3):
                if Z[i]==1:
                    op="+"
                else:
                    op="-"
                print(S[i]+op,end="")
            print(S[3]+"=7")
            exit()
        return

    for i in [1,-1]:
        Z.append(i)
        dfs(i)
        Z.pop()

dfs(0)