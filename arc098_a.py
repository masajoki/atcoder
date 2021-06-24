N=int(input())
S=input()
E=[0 for _ in range(N+1)]
E[0]=0
W=[0 for _ in range(N+1)]
W[0]=0
for i in range(len(S)):
    if S[i]=="E":
        E[i+1]=E[i]+1
        W[i+1]=W[i]
    else:
        E[i+1]=E[i]
        W[i+1]=W[i]+1


obey=N
for i in range(1,N+1):
    temp=E[-1]-E[i]+W[i-1]
    obey=min(obey,temp)
print(obey)
