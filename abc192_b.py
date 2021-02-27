S=input()
ans="Yes"
for i in range(len(S)):
    if (i+1)%2==0 and S[i].islower():
        ans="No"
        break
    elif (i+1)%2==1 and S[i].isupper():
        ans="No"
        break
print(ans)    