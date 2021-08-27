N,M=map(int,input().split())
S=[]
Sset=set()
Sint=[]
Sd=[]
SintD={}
for i in range(N):
    s=input()
    sint=int(s,2)
    S.append(s)
    if sint in SintD:
        SintD[sint]+=1
    else:
        SintD[sint]=1

for i in range(N-1):
    for j in range(i+1,N):
        a=int(S[i],2)
        b=int(S[j],2)
        xor=a^b
        sxor=format(xor,'05b')
        print(a,b,sxor,sxor.count('1'))

pass
# for i in range(2**10):
#     s=format(i,'020b')
#     count=s.count('1')
#     if count%2==1:
#         print(s)


