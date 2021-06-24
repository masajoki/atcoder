N=int(input())
Ng=[]
for i in range(3):
    Ng.append(int(input()))

if N in Ng:
    print("NO")
    exit()

for i in range(100):
    temp=0
    for j in (1,2,3):
        if N-j not in Ng:
            if N-j==0:
                print("YES")
                exit()
            else:
                temp=N-j
    if N!=temp:
        N=temp
    else:
        print("NO")
        exit()
print("NO")