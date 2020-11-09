N=int(input())
D=[]
for i in range(N):
    D.append(list(map(int,input().split())))

counter=0
for d in D:
    if d[0]==d[1]:
        counter+=1
        if counter==3:
            print("Yes")
            exit()
    else:
        counter=0
print("No")