S=input()
count=0
ans=0
i=0
while i<len(S):
    if i<len(S)-1 and S[i]=='2' and S[i+1]=="5":
        count+=1
        i+=2
    else:
        i+=1
        ans+=(count+1)*count//2
        count=0

ans+=(count+1)*count//2
print(ans)