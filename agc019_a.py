Q,H,S,D=map(int,input().split())
N=int(input())
q=Q*4
h=H*2
s=S
d=D/2
ans=0
buy=min(q,h,s)
if N>2 and d<buy:
    ans=N//2*D
    rest=N%2
    ans+=rest*buy
else:
    ans=N*buy
print(ans)

