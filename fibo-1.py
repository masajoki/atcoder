n=int(input())
fibo1=1
fibo2=2
fibo3=0

for i in range(4,99999):
    fibo3=fibo2+fibo1
    # print(i+4,fibo3)
    fibo1=fibo2
    fibo2=fibo3
    if n==i:
        print(fibo3)
        break
    

