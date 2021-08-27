def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]


N=int(input())
Plist=primes(N)

Ans=[k for k in range(N+1)]

def sumOfDiv(curSum,primeIndex,curDivCount):
    for i in range(N//Plist[primeIndex]+1):
        tempSum=curSum+i*Plist[primeIndex]
        if tempSum > N:
            Ans[curSum]=tempSum*curDivCount
            return
        else:
            if primeIndex+1<len(Plist):
                if i>0:
                    sumOfDiv(tempSum,primeIndex+1,curDivCount+i+1)
                else:
                    sumOfDiv(tempSum,primeIndex+1,curDivCount)
            else:
                Ans[tempSum]=tempSum*(curDivCount+i+1)
                return

sumOfDiv(0,0,0)

print(sum(Ans))
