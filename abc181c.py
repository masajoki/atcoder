N=int(input())
X=[]
Y=[]
for n in range(N):
    x,y=map(int,input().split())
    X.append(x)
    Y.append(y)


vertical=99999999999999
horizont=0

for i in range(N):
    points=set()
    for j in range(N):
        if i==j:
            continue
        else:
            dify=Y[j]-Y[i]
            difx=X[j]-X[i]
            if dify==0:
                points.add(horizont)
            elif difx==0:
                points.add(vertical)
            else:
                katamuki=dify/difx
                points.add(katamuki)
    
    if len(points)<(N-1):
        print('Yes')
        exit()
print('No')

