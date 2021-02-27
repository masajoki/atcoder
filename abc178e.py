x0=0
y0=0
x1=0
y1=10**9+10
N=int(input())
DIF0=[0 for _ in range(N)]
DIF1=[0 for _ in range(N)]

for i in range(N):
    x,y=map(int,input().split())
    DIF0[i]=abs(x0-x)+abs(y0-y)
    DIF1[i]=abs(x1-x)+abs(y1-y)

difmax=max(max(DIF0)-min(DIF0),max(DIF1)-min(DIF1))
print(difmax)