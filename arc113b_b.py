A,B,C=map(int,input().split())
d=[]
d.append((0,0,0,0))
d.append((1,1,1,1))
d.append((2,4,8,6))
d.append((3,9,7,1))
d.append((4,6,4,6))
d.append((5,5,5,5))
d.append((6,6,6,6))
d.append((7,9,3,1))
d.append((8,4,2,6))
d.append((9,1,9,1))

a=A%10
b=B%10
c=C%10

mod4=pow(B,C,4)
if mod4==0:
    mod4=4
ans=d[a][mod4-1]
print(ans)

