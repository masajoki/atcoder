K=int(input())
Nums=set()

def dfs(s,digits):
    n=int(s)
    if len(s)==digits:
        Nums.add(n)
    else:
        d=n%10
        if d-1>=0:
            dfs(s+str(d-1),digits)
        dfs(s+str(d),digits)
        if d+1<=9:
            dfs(s+str(d+1),digits)

d=1
while len(Nums)<=K+1:
    for i in range(10):
        dfs(str(i),d)
    d+=1

L=list(Nums)
L.sort()
print(int(L[K]))

