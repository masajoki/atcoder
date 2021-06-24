import math
for i in range(1,20):

    N=10**i
    print("-----"+str(i)+"-----")
    print(math.log10(N*math.log2(N)))
    print(math.log10(N*(N**0.5)))
    print(math.log10(N**2019))
    print(math.log10(2**N))
