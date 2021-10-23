import copy
S=input()
T=input()


if S==T:
    print("Yes")
    exit()

possible=False
temp2=[]

for j in range(len(S)):
    temp2.append(T[j])

temp=[]

for i in range(len(S)):
    temp.append(S[i])


for i in range(len(S)-1):
    temp3=copy.deepcopy(temp)
    for j in range(len(S)):
        if i==j:
            temp3[j]=temp[j+1]
            temp3[j+1]=temp[j]
        elif j==i+1:
            continue
        else:
            temp3[j]=temp[j]

    if temp3==temp2:
        possible=True


if possible:
     print("Yes")
else:
    print("No")

