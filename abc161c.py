N,K=map(int,input().split())
#N: 0<=N<=10**18
#K: 1<=K<=10**18

# f(x) x=|K-x|
# Nの最小値は？

if N==K:
    print(0)
elif N>K:
    if N%K==0:
        print(0)
    else:
        print(min(N%K,K%(N%K)))
elif K>N:
    print(min(N,K-N))
