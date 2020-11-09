S=input()
T=input()
minchange=len(T)
if len(S)==len(T):
    temp=0
    for i in range(len(S)):
        if S[i]!=T[i]:
            temp+=1
    minchange=min(minchange,temp)

for i in range(len(S)-len(T)):
    temp=0
    for j in range(len(T)):
        if S[i+j]!=T[j]:
            temp+=1
    minchange=min(minchange,temp)
print(minchange)