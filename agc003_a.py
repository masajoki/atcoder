T=list(set(input()))
T.sort()
S="".join(T)

if S in ('EW','NS',"ENSW"):
    print("Yes")
else:
    print("No")

