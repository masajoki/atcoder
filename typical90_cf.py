#084 - There are two types of characters（★3） 
# https://atcoder.jp/contests/typical90/tasks/typical90_cf
N=int(input())
S=input()
maru=[]
batsu=[]

ans=0
for i in range(N):
    if S[i]=="o":
        maru.append(i)
    else:
        batsu.append(i)

if len(batsu)==0 or len(maru)==0:
    print(0)
    exit()

j=0
for i in range(len(maru)):
    mi=maru[i]
    while j < len(batsu):
        bi=batsu[j]
        if bi > mi:
            ans+=N-bi
            break
        j+=1

j=0
for i in range(len(batsu)):
    bi=batsu[i]
    while j < len(maru):
        mi=maru[j]
        if bi < mi:
            ans+=N-mi
            break
        j+=1
     
print(ans)


