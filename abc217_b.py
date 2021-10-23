a=input()
b=input()
c=input()
S={}
S["ABC"]=False
S["ARC"]=False
S["AGC"]=False
S["AHC"]=False
S[a]=True
S[b]=True
S[c]=True

for v in S.keys():
    if S[v]==False:
        print(v)
        exit()
