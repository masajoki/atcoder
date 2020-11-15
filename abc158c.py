import math
A,B=map(int,input().split())
# x*0.08=A, x*0.1=B
# x=A/0.08 = A*12.5
# x=B/0.1 = B*10 
# B*10 <= x < (B+1)*10
# A*12.5 <= x < (A+1)*12.5

xAmin=math.ceil(A*12.5)
xAmax=math.floor((A+1)*12.5)
xBmin=B*10
xBmax=(B+1)*10
if xAmin >=xBmin:    
    for x in range(xAmin, xAmax+1):
        if x >= B*10 and x < (B+1)*10:
            print(x)
            exit()
else:
    for x in range(xBmin, xBmax+1):
        if x >= A*12.5 and x < (A+1)*12.5:
            print(x)
            exit()  
print(-1)