A,B=map(int,input().split())
taps=1
sockets=A
if B==1:
    print(0)
    exit()
while True:
    if B<=sockets:
        print(taps)
        exit()
    else:
        sockets+=(A-1)
        taps+=1
