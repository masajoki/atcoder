N=int(input())
A=[]
B=[]
AB=[]
C=[]
D=[]
CD=[]

if N==1:
    print("Yes")
    exit()

for i in range(N):
    a,b=map(int,input().split())
    AB.append([a,b])
AB.sort()

for i in range(N):
    c,d=map(int,input().split())
    CD.append([c,d])

        
for i in range(4):
    for i in range(N):
        c,d=CD[i]
        CD[i]=[d,c*-1]

    CD.sort()
    x,y=CD[0]
    abx,aby=AB[0]
    xdiff=abx-x
    ydiff=aby-y
    S=[]
    for j in range(N):
        x,y=CD[j]
        S.append([x+xdiff,y+ydiff])
    S.sort()
    if AB==S:
        print("Yes")
        exit()
print("No")
