s=list("abcdefghijklmnopqrstuvwxyz")

a=input()
for i in range(len(s)):
    if a==s[i]:
        print(s[i+1])
        break
    