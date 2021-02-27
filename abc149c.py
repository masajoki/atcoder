X=int(input())
nums=[ 0 for _ in range(2,X+10)]
for i in range(2,X+1):
    for j in range(i,X+1):
        if i*j<(X+1) :
            if nums[i*j]==0:
                nums[i*j]=1
        else:
            break

for i in range():
    if nums[i]==0:
        print(i)
        exit()
