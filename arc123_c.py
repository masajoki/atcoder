T=int(input())
Case=[]
digi={}

digi[0]=(4,5,6,7,8,9)
digi[1]=(1,4,5,6,7,8,9)
digi[2]=(1,2,4,5,6,7,8,9)
digi[3]=(1,2,3,5,6,7,8,9)
digi[4]=(2,3,4,5,6,7,8,9)
digi[5]=(2,3,4,5,6,7,8,9)
digi[6]=(2,3,4,5,6,7,8,9)
digi[7]=(3,4,5,6,7,8,9)
digi[8]=(3,4,5,6,7,8,9)
digi[9]=(3,4,5,6,7,8,9)
for i in range(T):
    c=input()
    Case.append(c)


for C in Case:
    ans=0
    for c in C:
        if ans in digi[int(c)]:
            continue
        for d in digi[int(c)]:
            if d>ans:
                ans=d
                break
    print(ans)


