import itertools
import copy
S1=input()
S2=input()
S3=input()
abc=set()
ABC=S1+S2+S3
for a in ABC:
    abc.add(a)

if len(abc)>10:
    print("UNSOLVABLE")
    exit()
Labc=list(abc)
dic={}
P=itertools.permutations(range(10),len(abc))

for pl in P:
    for i in range(len(abc)):
        dic[Labc[i]]=pl[i]

    if dic[S1[0]]==0 or dic[S2[0]]==0 or dic[S3[0]]==0:
        continue
    else:
        T1=0
        for i in range(len(S1)):
            T1+=dic[S1[i]]*10**(len(S1)-1-i)

        T2=0
        for i in range(len(S2)):
            T2+=dic[S2[i]]*10**(len(S2)-1-i)

        T3=0
        for i in range(len(S3)):
            T3+=dic[S3[i]]*10**(len(S3)-1-i)

        if int(T1)+int(T2)==int(T3):
            print(T1)
            print(T2)
            print(T3)
            exit()
print("UNSOLVABLE")
