N=int(input())
c=input()
count=0
leftposi=len(c)-1
for i in range(N):
    if i  >= leftposi:
        print(count)
        exit()
    if c[i]=='W' and c[leftposi]=='R':
        count+=1
        leftposi-=1
    elif  c[i]=='W' and c[leftposi]=='W':
        for j in range(leftposi, i, -1):
            if c[j]=='R':
                count+=1
                leftposi=j
                break
            leftposi=j
            

        
