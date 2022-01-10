# typical90_aj.py
# 036 - Max Manhattan Distance（★5)
# 45度変換するというか、x,yをx-y, x+yに変換しておくと、
#簡単に比べられるようになる  
N,Q=map(int,input().split())
X=[]
Y=[]
xmax=-10**10
ymax=-10**10
xmin=10**10
ymin=10**10
for i in range(N):
    x,y=map(int,input().split())
    x,y=x+y,x-y #これで４５度変換というか原点からのマンハッタン距離を

    X.append(x) #45度変換する
    Y.append(y) #45度変換する
    xmax=max(x,xmax)
    xmin=min(x,xmin)
    ymax=max(y,ymax)
    ymin=min(y,ymin)
queries=[]
for i in range(Q):
    q=int(input())
    queries.append(q-1)

for i in queries:
    t=max(abs(xmax-X[i]),abs(xmin-X[i]),abs(ymax-Y[i]),abs(ymin-Y[i]))
    print(t)