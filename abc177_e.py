N=int(input())
A=list(map(int,input().split()))
F=[0 for _ in range(10**6+10)]
import collections
def prime_factorize(n): #因数分解
    global F
    flag=False
    while n % 2 == 0:
        flag=True
        n //= 2
    if flag:
        F[2]+=1
    f = 3
    flag=False
    while f * f <= n:
        if n % f == 0:
            if flag==False:
                F[f]+=1
                flag=True
            n //= f
        else:
            flag=False
            f += 2
    if n != 1 and n!=f:
        F[n]+=1
count1=0
for a in A:
    if a==1:
        count1+=1
    else:
        prime_factorize(a)

if F.count(1)==N-count1:
    print("pairwise coprime")
    exit()
for i in range(2,10**6+10):
    if F[i]==0:
        continue
    elif count1>0:
        print("setwise coprime")
        exit()
    elif F[i]>=N-count1:
        print("not coprime")
        exit()
print("setwise coprime")