N,S,D=map(int,input().split())
X=[]
Y=[]
damage=False
for i in range(N):
    x,y=map(int,input().split())
    if x>=S or y<=D:
        continue
    else:
        damage=True

if damage:
    print("Yes")
else:
    print("No")
