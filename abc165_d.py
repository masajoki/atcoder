A,B,N=map(int,input().split())

tempmax=-1
for i in range(1,N+1):
    temp=int(A*i/B)-A*int(i/B)
    print(A*i/B,A*int(i/B))
    if tempmax >= temp:
        # print(int((A*(i-1)-A*(i-1)%B)/B - (A*((i-1)-(i-1)%B))/B))
        print(int(A*(i-1)/B)-A*int((i-1)/B))
        exit()
    else:
        tempmax=temp

print(int((A*i-A*i%B)/B - (A*(i-i%B))/B))
