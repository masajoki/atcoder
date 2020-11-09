from sys import stdin

def main():

    n=int(input())
    As=list(map(int, stdin.readline().split()))
    As.sort()
    primes=[]
    answers=[]


    primes.append(100003)
    last=0


    found=True

    for a in As:
        if last == a:
            if found == False:
                answers.pop(-1)
            last=a
            found=True
            continue

        for p in primes:
            if a % p == 0 :
                found=True
                break
            else:
                found=False

        if found==False:
            if a!=1:
                primes.append(a)
            answers.append(a)
            last=a

        else:
            last=a

    print (len(answers))

if __name__ == '__main__':
    main()