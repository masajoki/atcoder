N=int(input())
for p5 in range(1,26):
    for p3 in range(1,38):
        if 3**p3 + 5**p5 == N:
            print(str(p3)+" "+str(p5))
            exit()
print("-1")