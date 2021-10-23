N,X=map(int,input().split())
A=[]
B=[]
C=[]
D=[]

ans_max=0
ans_min=10**10
for i in range(N):
    a,b,c,d=map(int,input().split())
    temp=X-a
    if temp<0:
        ans_max=max(ans_max,b)
        ans_min=min(ans_min,b)
        continue
    
    r=temp//c
    ans_max=max(ans_max,b+(r+1)*d)
    ans_min=min(ans_min,b+(r+1)*d)

print(ans_min,ans_max)
