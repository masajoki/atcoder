S=input()
ans=[]
for s in S:
    if s in ("0","1"):
        ans.append(s)
    else:
        if len(ans)>0:
            ans.pop()
print("".join(ans))