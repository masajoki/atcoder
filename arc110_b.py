import math
N=input()
T=input()

if len(T)==1:
    if T=="0":
        print(10**10)
    elif T=="1":
        print(2*10**10)
    exit()
elif len(T)==2:
    if T=="11" or T=="10":
        print(10**10)
    elif  T=="01":
        print(10**10-1)
    else:
        print(0)
    exit()
elif len(T)==3:
    if T in ("000","001","010","100","111"):
        print(0)
    elif T in ("011","101"):
        print(10**10-1)
    elif T in ("110"):
        print(10**10)
    exit()
elif len(T)==4:
    if T in ("1101","1011","0110"):
        print(10**10-1)
    else:
        print(0)
    exit()
patternstart=-1
breakpoint=-1
i=0
while i<len(T):
    ｔ=T[i:i+3]
    if t=="110":
        if patternstart==-1:
            patternstart=i
        i+=3
    else:
        if patternstart!=-1:
            breakpoint=i
            break
        i+=1
if patternstart==-1:
    print(0)
    exit()

header=""
trailer=""
if patternstart!=-1:
    header=T[:patternstart]
if breakpoint!=-1:
    trailer=T[breakpoint:]
if header not in ("10","0","") or trailer not in ("1","11",""):
    print(0)
else:
    h=math.ceil(len(header)/3)
    t=math.ceil(len(trailer)/3)
    b=(len(T)-len(header)-len(trailer))//3
    ans=10**10-b-t-h+1
    print(ans)
    




    