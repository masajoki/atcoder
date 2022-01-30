#abc236_c.py
N,M=map(int,input().split())
S=list(input().split())
T=list(input().split())
Tset=set(T)
for s in S:
    if s in Tset:
        print("Yes")
    else:
        print("No")
    