O=input()
E=input()
for i in range(max(len(O),len(E))):
    if i < len(O):
        print(O[i],end="")
    if i < len(E):
        print(E[i],end="")
print()