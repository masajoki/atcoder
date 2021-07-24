N=int(input())
A,B,C=map(int,input().split())

ans=99999
for a in range(min(10000,N//A+1)):
    rest=N
    if a!=0:
        rest=N-a*A
    for b in range(min(10000,rest//B+1)):
        if b!=0:
            temp=rest-b*B
        else:
            temp=rest
        if temp>=0 and temp%C==0:
            ans=min(ans,a+b+temp//C)

print(ans)    
    
