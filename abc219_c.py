X=input()
ABC='abcdefghijklmnopqrstuvwxyz'
Dic={}
DicR={}

for i in range(26):
    Dic[ABC[i]]=X[i]
    DicR[X[i]]=ABC[i]

N=int(input())
S=[]
forSort=[]

for i in range(N):
    st=input()
    S.append(st)

    temp=""
    for s in st:
        temp=temp+DicR[s]
    forSort.append(temp)

forSort.sort()

for st in forSort:
    temp=""
    for s in st:
        temp=temp+Dic[s]
    print(temp)