S=input()
Slen=len(S)
ans=0
for i in range(Slen):
    if S[i]=='U':
        ans+=Slen-(i+1)+i*2
    else:
        ans+=2*(Slen-(i+1))+i
print(ans)
        

