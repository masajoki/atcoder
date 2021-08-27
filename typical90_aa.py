N=int(input())
S=set()
I=[]

for i in range(N):
    i=input()
    I.append(i)
for i in range(N):
    s=I[i]
    if s in S:
        continue
    else:
        print(i+1)
        S.add(s)
