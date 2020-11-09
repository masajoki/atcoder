n=int(input())
A=list(map(int,input().split()))
A.sort()
Adict={}
q=int(input())
B=[]
C=[]
for i in range(q):
    b,c=map(int,input().split())
    B.append(b)
    C.append(c)

S=[]

last=0
for a in A:
    if last!=a:
        Adict[a]=1
    else:
        Adict[a]+=1
    last=a

sum=0
for a in Adict:
    sum+=Adict[a]*a


for index ,b in enumerate(B):
    if b in Adict:
        c=C[index]
        sum=sum-b*Adict[b]+c*Adict[b]
        if c in Adict:
            Adict[c]+=Adict[b]
        else:
            Adict[c]=Adict[b]
        del Adict[b]
        S.append(sum)
    else:
        S.append(sum)

for s in S:
    print(s)