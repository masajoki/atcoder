N=int(input())
ope=[]
while N!=1:
    if N%2==0:
        N//=2
        ope.append("B")
    else:
        N-=1
        ope.append("A")

ope.reverse()
print("A"+"".join(ope))

    