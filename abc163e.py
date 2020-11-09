n=int(input())
A=[0]*n
B=[0]*n

for i in range(0,n):
    A[i],B[i]=map(int,input().split())

medA=0
medB=0

if len(A)%2==0:
    i=int(n/2)-1

    medA=(A[i]+A[i+1])/2
    medB=(B[i]+B[i+1])/2
    print (medB-medA+1)
