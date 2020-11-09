x,K,D=map(int,input().split())
X=abs(x)
ans=0
if D<X and K*D > X:
    if (K-X//D)%2==0:
        ans=X%D
    else:
        ans=D-X%D
    
elif D<X and K*D<=X:
    ans=X-D*K
elif D>=X:
    if K%2 ==0:
        ans=X
    else:
        ans=D-X
print(abs(ans))
