N=int(input())
S=[]
for i in range(2**N):
    s=[]
    for j in range(N):
        if i >> j & 1 ==1:
            s.append('(')
        else:
            s.append(')')
    S.append(s)
ans=[]
for s in S:
    T=list(s)
    temp=0
    for t in T:
        if temp<0:
            continue
        if t=='(':
            temp+=1
        else:
            temp-=1
    if temp==0:
        ans.append(s)
ans.sort()

for a in ans:
    print("".join(a))


        
    
