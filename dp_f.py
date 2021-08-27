S=input()
T=input()

ST=[0 for _ in range(len(S))]
for i in range(len(S)):
    for j in range(i,len(T)):
        if S[i]==T[i]:
            
