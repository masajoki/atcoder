N=input()
A=list(map(int,input().split()))
odds=0
for a in A:
    if a%2==1:
        odds+=1

if odds%2==1:
    print("NO")
else:
    print("YES")