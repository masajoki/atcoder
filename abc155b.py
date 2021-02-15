N=int(input())
A=list(map(int,input().split()))
ans="APPROVED"
for a in A:
    if a % 2 == 1 or a % 6 == 0 or a % 10 == 0:
        continue
    else:
        ans="DENIED"
        break
print(ans)
