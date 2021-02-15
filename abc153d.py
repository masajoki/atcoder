H=int(input())

divcount=0
while H!=1:    
    divcount+=1
    if H%2==0:
        H/=2
    else:
        H=H//2

ans=0
for i  in range(0,divcount+1):
    ans+=2**i
print(ans)
