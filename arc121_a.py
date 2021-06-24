N=int(input())
X=[]
Y=[]
Dist=[]
for i in range(N):
    x,y=map(int,input().split())
    X.append((x,i))
    Y.append((y,i))

X.sort()
Y.sort()

for i,j in ((-1,0),(-1,1),(-2,0),(-2,1)):
    Dist.append((X[i][0]-X[j][0],X[i][1],X[j][1]))
    Dist.append((Y[i][0]-Y[j][0],Y[i][1],Y[j][1]))

Dist.sort()

if Dist[-1][1]==Dist[-2][1] and Dist[-1][2]==Dist[-2][2]: 
    print(Dist[-3][0])
else:
    print(Dist[-2][0])
