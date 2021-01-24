r,D,x2000=map(int,input().split())
x=r*x2000-D
print(x)
for i in range(9):
    x=r*x-D
    print(x)