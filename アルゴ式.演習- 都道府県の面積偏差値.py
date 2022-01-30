import statistics
X=[]
S=[]
for i in range(47):
    x,s=input().split()
    X.append(x)
    S.append(int(s))

avg1=statistics.mean(S)
pstd=statistics.pstdev(S)

for i in range(47):
    t=round(50+10*(S[i]-avg1)/pstd,2)
    print(X[i],'{:.2f}'.format(t))
