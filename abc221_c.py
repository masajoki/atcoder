from itertools import permutations
S=input()
N=int(S)
Slist=list(S)
P=permutations(Slist)

slen=len(S)
ansmax=0
for s in P:
    for i in range(1,slen):
        s1=s[:i]
        s2=s[i:]
        if s1[0]=='0' or s2[0]=='0':
            continue
        else:
            s1i=int("".join(s1))
            s2i=int("".join(s2))
            ansmax=max(s1i*s2i,ansmax)

print(ansmax)
