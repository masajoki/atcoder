N=int(input())
S=[]
T=[]
Names=set()
for i in range(N):
    name=input()
    Names.add(name)

if len(Names)==N:
    print("No")
else:
    print("Yes")
    