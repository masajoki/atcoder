N=int(input())
S=[]
T=[]
for i in range(N):
    S.append(input())

temp=0
for s in S:
    if s=="OR":
        T.append(temp)
        temp=0
    else:
        temp+=1

ans=2**(N+1)
T.append(temp)

temp=1
for t in T:
    temp*=(2**(t+1)-1)

print(ans-temp)