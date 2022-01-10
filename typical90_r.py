import math
T=int(input())
L,X,Y=map(int,input().split())
Q=int(input())
E=[]
for i in range(Q):
    E.append(int(input()))

#Eから水平からの角度を計算する
def calcR(e):
    r=-2*math.pi*(e/T)-math.pi/2.0
    return r

#e のz計算する
def calcZ(rad):
    z=L/2.0+L/2.0*math.sin(rad)
    return z

#e のyを計算する
def calcY(rad):
    y=L/2.0*math.cos(rad)
    return y

def dis_e_to_statue(e):
    r=calcR(e)
    y=calcY(r)
    z=calcZ(r)
    hen1=((Y-y)**2+X**2)**0.5
    hen2=z
    r=math.atan(hen2/hen1)
    d=math.degrees(r)
    return d

for i in range(Q):
    d=dis_e_to_statue(E[i])
    print(d)


