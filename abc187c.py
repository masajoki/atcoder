
N=int(input())
S=[]
for i in range(N):
    s=input()
    S.append(s)

D={}
for s in S:
    if s not in D:
        D[s]=1
    else:
        D[s]+=1
# print(D)
for k in D.keys():
    st='!'+k
    if st in D:
        print(k)
        exit()
print("satisfiable")
