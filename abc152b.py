a,b=map(int,input().split())
tempa=0
tempb=0
for i in range(b):
    tempa+=a*10**i

for i in range(a):
    tempb+=b*10**i

hoge=[str(tempa),str(tempb)]
hoge.sort()
print(hoge[0])