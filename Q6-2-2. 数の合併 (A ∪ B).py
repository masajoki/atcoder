N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
abset=set()
for a in A:
    abset.add(a)
for b in B:
    abset.add(b)

absetlist=list(abset)
absetlist.sort()
for abl in absetlist:
    print(abl)