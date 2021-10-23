import sys
sys.setrecursionlimit(10**7)
K,S,T=map(int,input().split())

def level(x):
    if x==1:
        return 3
    else:
        return 3+level(x-1)*2

for i in range(1,50):
    print (level(i))