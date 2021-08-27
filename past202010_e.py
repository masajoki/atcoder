import itertools
N=int(input())
S=list(input())
Srev=list(reversed(S))
patterns=list(itertools.permutations(S,N))
for p in patterns:
    pl=list(p)
    if pl!=S and pl!=Srev:
        print("".join(p))
        exit()
print("None")
