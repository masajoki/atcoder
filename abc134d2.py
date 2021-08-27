M=int(input())
B=list(map(int,input().split()))

for i in range(M):
    sumtemp=0
    j=1
    while (i+1)*j-1<M:
        sumtemp+= B[(i+1)*j-1]
        j+=1
    if sumtemp%2 != B[i]:
        print(-1)
        exit()

count=0
for i in range(M):
    if B[i]==1:
        count+=1

print(count)
for i in range(M):
    if B[i]==1:
        print(i+1)






