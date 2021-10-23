vowels='AEIOUaeiou'
S=input()
for s in S:
    if s in vowels:
        continue
    else:
        print(s,end="")
print()