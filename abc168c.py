import math
ABHM=input().split(' ')
A=int(ABHM[0])
B=int(ABHM[1])
H=int(ABHM[2])
M=int(ABHM[3])

radian=(11.0/360*M-H/6.0)*math.pi
C=abs(A**2 + B**2 -2*A*B*math.cos(radian) )**0.5
print(C)
