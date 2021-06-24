N=int(input())

A=list(map(int,input().split()))
B=list(map(int,input().split()))

temp=(min(B)-max(A)+1)
ans=max(0,temp)
print(ans)