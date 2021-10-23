N,K=map(int,input().split())

if N==0:
    print(0)
    exit()
T=list(str(N))
temp=0

for k in range(K):
    for i in range(len(T)):
        temp+=int(T[i])*8**(len(T)-1-i)

    T=[]
    for i in range(20,-1,-1):
        p=temp//9**i
        if p==8:
            p=5
        temp%=9**i
        T.append(p)

prefix=True
for i in range(21):
    if T[i]==0 and prefix==True:
        continue
    else:
        prefix=False
        print(T[i],end="")
print()

