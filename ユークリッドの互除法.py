#ユークリッドの互除法練習

def gcd(a,b):
    if a<b:
        a,b=b,a
    r=a%b
    if r==0:
        return b
    else:
        return gcd(b,r)

# import time
# import math


#時間計測してみると埋め込みのほうが数倍速い
# t1=time.time()
# print(gcd(1893289038219089458905830985904829063890212,32))
# t2=time.time()
# print(t2-t1)



# t1=time.time()
# print(math.gcd(1893289038219089458905830985904829063890212,32))
# t2=time.time()
# print(t2-t1)
