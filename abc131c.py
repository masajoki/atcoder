import math
A,B,C,D=map(int,input().split())
cdgcd=math.gcd(C,D)
koubaisu=C*D//cdgcd

t1=B//C
t2=(A-1)//C
t3=B//D
t4=(A-1)//D
t5=B//koubaisu
t6=(A-1)//koubaisu

ans=(B-A+1)-t1+t2-t3+t4+t5-t6
print(ans)