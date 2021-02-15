N,Q=map(int,input().split())
S=input()
L=[]
R=[]
for i in range(Q):
    l,r=map(int,input().split())
    L.append(l)
    R.append(r)
for i in range(Q):
    s=S[L[i]-1:R[i]]
    print(s.count('AC'))
