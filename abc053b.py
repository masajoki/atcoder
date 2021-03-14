import collections
S=input()
c=collections.Counter(S)
pairs=0
mod=0
for v in c.values():
    pairs+=v//2
    mod+=v%2

if mod!=0:
    minkaibun=(pairs//mod)*2+1
else:
    minkaibun=pairs*2
print(minkaibun)

