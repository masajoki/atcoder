N=int(input())
S=[]
W=set()

for i in range(N):
    S.append(input())


lastc=S[0][-1]
W.add(S[0])
for i in range(1,N):
    if S[i][0]==lastc and S[i] not in W:
        lastc=S[i][-1]
        W.add(S[i])
    else:
        print("No")
        exit()
print("Yes")
