x,y=map(int,input().split())
if abs(x)<abs(y):
    if 0<=x and 0<=y:
        print(y-x)
    elif x<0 and y<0:
        print(abs(y)-abs(x)+2)
    elif x<0 and y>=0:
        print(abs(y)-abs(x)+1)
    elif x>=0 and y<0:
        print(abs(y)-abs(x)+1)
    else:
        print(abs(y)-abs(x)+1)
elif abs(x)>abs(y):
    if 0<=x and 0<=y:
        print(x-2+2)
    elif x<0 and y<0:
        print(abs(x)-abs(y))
    elif x<0 and y>=0:
        print(abs(x)-abs(y)+1)
    elif x>=0 and y<0:
        print(abs(x)-abs(y)+1)
    else:
        print(abs(x)-abs(y)+1)
else:
    if 0<=x and 0<=y:
        print(0)
    elif x<0 and y<0:
        print(0)
    else:
        print(1)
