N=int(input())
A=[]
B=[]
for i in range(N):
    a,b=map(int,input().split())

    A.append(a)
    B.append(b)

ans=0
added=0
temp=0
for i in range(N-1,-1,-1):
    A[i]+=added
    if A[i]%B[i]==0:
        temp=0
    else:
        temp=B[i]-A[i]%B[i]
        A[i]+=temp
        added+=temp
print(added)