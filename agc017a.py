N,P=map(int,input().split())
A=list(map(int,input().split()))

even=0 
odd=0

for a in A:
    if a%2==0:
        even+=1
    else:
        odd+=1

evens=2**even
odds=2**odd//2

ans=0

if P==0 and odd==0:
    ans=evens
elif P==0 and odd!=0:
    ans=evens*odds
elif P==1 and odd==0:
    ans=0
elif P==1 and odd!=0:
    ans=evens*odds

print(ans)