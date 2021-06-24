from itertools import product
H,W,A,B=map(int,input().split())

seed=str(0)*B
temp=""
for i in range(A+1):
    temp="1"*(i)+"2"*(A-i)
    print(seed+temp)