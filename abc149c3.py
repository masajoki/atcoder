X=int(input())

maxdiv=int(X**0.5)+1
if X in [2,3,5,7,11,13,17]:
    print(X)
    exit()

while True:
    found=0
    for i in range(2,maxdiv+1):
        if X%i==0:
            X+=1
            maxdiv+=1
            break
        elif i==maxdiv:
            print(X)
            exit()    

    
