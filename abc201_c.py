S=input()
A=[]
for i in range(10000):
    s=str(i)
    sz=s.zfill(4)
    A.append(sz)

ans=0
for a in A:
    OK=True
    for i in range(10):
        temp=str(i)
        if S[i]=='o':
            if temp not in a:
                OK=False
                break
        elif S[i]=='x':
            if temp in a:
                OK=False
                break
    if OK:
        ans+=1
    
print(ans)