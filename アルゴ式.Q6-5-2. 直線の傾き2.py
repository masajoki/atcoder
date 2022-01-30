N,a,b=map(int,input().split())
def katamuki(a,b):
    return (b**2-a**2)/(b-a)



for i in range(N):
    print (katamuki(a,b))
    b=(a+b)/2