N=list(input())
N.reverse()
T=[]

zero=0
for s in N:
    if s=='0':
        zero+=1
    else:
        break

T=N[zero:]
TR=list(reversed(T))

if TR==T:
    print("Yes")
else:
    print("No")

