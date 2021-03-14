Sd=list(input())
T=list(input())
N=len(Sd)-len(T)+1
Sd.reverse()
T.reverse()

for i in range(N):
    St=[]
    matched=True
    for s in Sd:
        if s=="?":
            St.append("a")
        else:
            St.append(s)
    for j in range(len(T)):        
        if Sd[i+j]!="?" and T[j]!=Sd[i+j]:
            matched=False
            break
        elif Sd[i+j]=="?" or Sd[i+j]== T[j]:
            St[i+j]=T[j]
    if matched==True:
        ans=list(St)
        ans.reverse()
        print("".join(ans))
        exit()
print("UNRESTORABLE")
