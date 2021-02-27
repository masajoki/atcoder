S=input()
O=0
X=0
for s in S:
    if s=='o':
        O+=1
        X=0
    elif s=='x':
        X+=1
        O=0
    if O>=3:
        print("o")
        exit()
    elif X>=3:
        print("x")
        exit()

print("draw")
