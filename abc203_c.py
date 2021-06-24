N,K=map(int,input().split())
A=[]
B=[]
AB=[]

for i in range(N):
    a,b=map(int,input().split())
    A.append(a)
    B.append(b)
    AB.append((a,b))

AB.sort()

pos=0
for i in range(N):
    a,b=AB[i]
    if pos+K>=a:
        K-=(a-pos)
        pos=a
        K+=b
    elif pos+K<a:
        break
if pos+K>=10**100:
    print(10**100)
else:
    print(pos+K)





