S=input()
T=input()
for i in range(len(S)):
    temp=S[len(S)-1-i:]+S[:len(S)-1-i]
    if T==temp:
        print("Yes")
        exit()
print("No")