S=list(input())
l=len(S)
countw=0
steps=0
for i in range(l):
    if S[i]=='W':
        countw+=1
        steps+=(1+i-countw)

print(steps)
