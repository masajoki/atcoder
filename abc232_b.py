S=input()
T=input()
N=len(S)
sn=ord(S[0])
tn=ord(T[0])
if sn<tn:
    sn+=26
d=sn-tn
for i in range(N):
    sn=ord(S[i])
    tn=ord(T[i])
    if sn<tn:
        sn+=26
    if sn-tn!=d:
        print("No")
        exit()
print("Yes")
