X,Y=map(int,input().split())
rest=Y-X
if X>=Y:
    print(0)
elif rest%10==0:
    print(rest//10)
else:
    print(rest//10+1)
