N=input()
sum=0
for n in N:
    sum+=int(n)

if sum % 9 ==0:
    print("Yes")
else:
    print("No")
