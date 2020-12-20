N=int(input())
S=[]
P=[]
SP=[]
for i in range(N):
    s,p=input().split()
    S.append(s)
    P.append(p)
    sp=s+" "+str(p)
    SP.append(sp)
S.sort()
P.sort()
P.reverse()

for i in range(N):
    sp=S[i]+" "+str(P[i])
    key=SP.index(sp)
    print(key)
