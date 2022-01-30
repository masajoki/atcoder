#abc237_c.py
S=list(input())
def removePrea(A):
    B=[]
    prea=True
    for i in range(len(A)):
        if A[i]!='a':
            prea=False
        if prea==False:
            B.append(A[i])
    return B

def countPre(A):
    prea=True
    count=0
    for i in range(len(A)):
        if A[i]!='a':
            return count
        else:
            count+=1
    return count

preacnt=countPre(S)
Srev=list(reversed(S))
trailcnt=countPre(Srev)
if preacnt>trailcnt:
    print("No")
    exit()

A1=removePrea(S)
A2=list(reversed(A1))
A3=removePrea(A2)
A4=list(reversed(A3))
if A3 == A4:
    print("Yes")
else:
    print("No")