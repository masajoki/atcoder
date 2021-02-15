import collections
St=input()
Sint=int(St)
S=list(St)
S.sort()
Sstr="".join(S)

if Sint<10 and Sint==8:
    print("Yes")
    exit()

patterns=[]
for i in range(2,13):
    t=i*8
    ts=list(str(t))
    if ts.count("0")>0:
        continue
    ts.sort()
    patterns.append("".join(ts))

if Sint<100:
    for ts in patterns:
        if Sstr.find(ts)!=-1:
            print("Yes")
            exit()
        

patterns=[]
for i in range(13,126):
    t=i*8
    ts=list(str(t))
    if ts.count("0")>0:
        continue
    ts.sort()
    patterns.append("".join(ts))


for ts in patterns:
    if Sstr.find(ts)!=-1:
        print("Yes")
        exit()
print("No")