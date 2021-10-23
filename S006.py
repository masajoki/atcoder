import math
a,b,x,y,r,S,L=map(int,input().split())
Xdist=(L*math.cos(math.radians(S))) % (2*a)
Ydist=(L*math.sin(math.radians(S))) % (2*b)

ansX=-999
ansY=-999


Xdis=Xdist%(2*a)
Ydis=Ydist%(2*b)

if 0<=Xdis+x<=a:
    ansX=Xdis+x

elif a< Xdis+x <=2*a:
    ansX=-2*a-Xdis+x
elif 2*a<Xdis+x:
    ansX=-2*a+Xdis+x
elif -a<=Xdis+x<0:
    ansX=-Xdis-x
elif Xdis+x<-a:
    ansX=2*a-Xdis+x

if 0<=Ydis+y<=b:
    ansY=Ydis+y

elif b< Ydis+y <=2*b:
    ansY=b+y-Ydis
elif 2*b<Ydis+y:
    ansY=-2*b+Ydis+y

elif -b<=Ydis+y<0:
    ansY=-Ydis-y
elif Ydis+y<-b:
    ansY=2*b-Ydis+y

print(ansX,ansY)