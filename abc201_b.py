N=int(input())
S=[]
T=[]
ST=[]
for i in range(N):
    s,t=input().split()
    S.append(s)
    T.append(int(t))
    ST.append((int(t),s))
ST.sort(reverse=True)
print(ST[1][1])


