H,A=map(int,input().split())
rest=0
if H%A!=0:
    rest=1
print(H//A+rest)