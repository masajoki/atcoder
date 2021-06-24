N=int(input())
indeed=list("indeednow")
indeed.sort()

S=[]
for i in range(N):
    temp=list(input())
    temp.sort()
    S.append(temp)

for s in S:
    if s==indeed:
        print("YES")
    else:
        print("NO")

