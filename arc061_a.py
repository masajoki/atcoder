S=input()
ans=0
for i in range(2**(len(S)-1)):
    temp=int(S[0])
    for j in range(len(S)-1):
        if i>>j&1==1:
            ans+=temp
            temp=int(S[j+1])
        else:
            temp=temp*10+int(S[j+1])
    ans+=temp
print(ans)

