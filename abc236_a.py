S=input()
a,b=map(int,input().split())

for i in range(len(S)):
    if i==a-1:
        print(S[b-1],end="")
    elif i==b-1:
        print(S[a-1],end="")
    else:
        print(S[i],end="")

print()
