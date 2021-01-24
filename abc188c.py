N=int(input())
A=list(map(int,input().split()))
c1=max(A[:2**N//2])
c2=max(A[2**N//2:])
winnerscore=min(c1,c2)
ans=A.index(winnerscore)+1
print(ans)