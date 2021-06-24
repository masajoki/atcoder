T=int(input())
N=[]
S1=[]
S2=[]
S3=[]
for _ in range(T):
    N.append(int(input()))
    S1.append(input())
    S2.append(input())
    S3.append(input())

for i in range(T):
    print("0"*N[i]+"1"*N[i]+"0")
