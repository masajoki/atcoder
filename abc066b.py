S=input()
for i in range(1,len(S)):
    if (len(S)-i)%2==1:
        continue
    sublen=(len(S)-i)//2
    a= S[:sublen]
    b= S[sublen:sublen+sublen]
    if a==b:
        print(len(S)-i)
        exit()
