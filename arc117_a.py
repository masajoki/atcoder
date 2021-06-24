A,B=map(int,input().split())

def calc(Plus,Minus):
    T=[]
    Ans=[]
    for i in range(1,Plus+1):
        T.append(i)
        Ans.append(i)
    for i in range(Minus-1):
        Ans.append(-1*T[i])
    Ans.append(-1*sum(T[Minus-1:]))
    return Ans
def calc2(Plus,Minus):
    T=[]
    Ans=[]
    for i in range(1,Minus+1):
        T.append(i)
        Ans.append(-1*i)
    for i in range(Plus-1):
        Ans.append(T[i])
    Ans.append(sum(T[Plus-1:]))
    return Ans

if A>B:
    Ans=calc(A,B)
elif B>A:
    Ans=calc2(A,B)
else:
    Ans=[]
    for i in range(1,A+1):
        Ans.append(i)
        Ans.append(-1*i)

for a in Ans:
    print(a, end=" ")
print()



