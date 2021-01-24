#これどこでも3手以内で行ける
r1,h1=map(int,input().split())
r2,h2=map(int,input().split())
x=abs(r2-r1)
y=abs(h2-h1)

if x==0 and y==0:
    print(0)
elif x==y:
    print(1)
elif (x+y)<=3:
    print(1)
elif (x+y)%2==0:
    print(2)
elif (x+y)<=6: #マンハッタン距離が6以内（たてよこいどう）
    print(2)
else:
    dif=abs(x-y)
    if dif <=3:
        print(2)
    else:
        print(3)
