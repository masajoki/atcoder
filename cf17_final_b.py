S=input()
a,b,c=0,0,0
for s in S:
    if s=="a":
        a+=1
    elif s=="b":
        b+=1
    else:
        c+=1
if max(a,b,c) - min(a,b,c) <=1:
    print("YES")
else:
    print("NO")