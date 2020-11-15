temp=set()
N=int(input())
A=list(map(int,input().split()))
for a in A:
    temp.add(a)
if len(temp)==N:
    print("YES")
else:
    print("NO")