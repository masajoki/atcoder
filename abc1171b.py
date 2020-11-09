Num,k=map(int,input().split())
P=list(map(int,input().split()))
P.sort()
temp=0
for i in range(k):
    temp+=P[i]
print(temp)