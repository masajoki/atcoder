import itertools
import copy

N=int(input())
A=list(map(int,input().split()))
Am=[ [] for _ in range(200)]
Am2=[]
for i in range(N):
    t=A[i]%200
    Am[t].append(i)
    Am2.append(t)


for i in range(200):
    if len(Am[i])>1:
        print("Yes")
        print(1,Am[i][0]+1)
        print(1,Am[i][1]+1)
        exit()

Hoge=copy.deepcopy(Am)

for i in range(200):
    if len(Am[i])>0:
        Am[i]=[Hoge[i]]

indexes=[i for i in range(N)]
combis=itertools.combinations(indexes, 2)
for cb in combis:
    t=(A[cb[0]]+A[cb[1]])%200
    if len(Am[t])==1:
        print("Yes")
        for a in Am[t]:
            print(len(a),end=" ")
            for b in a:
                print(b+1, end=" ")
            print()
        print(len(cb),end=" ")
        for a in cb:
            print(a+1, end=" ")
        print()
        exit()
    else:
        Am[t].append(cb)

if N>2:
    combis=itertools.combinations(indexes, 3)
    for cb in combis:
        t=(A[cb[0]]+A[cb[1]]+A[cb[2]])%200
        if len(Am[t])==1:
            print("Yes")
            for a in Am[t]:
                print(len(a),end=" ")
                for b in a:
                    print(b+1, end=" ")
                print()
            print(len(cb),end=" ")
            for a in cb:
                print(a+1, end=" ")
            exit()
        else:
            Am[t].append(cb)

print("No")
