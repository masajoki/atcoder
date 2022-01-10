#arc132_b.py
N=int(input())
P=list(map(int,input().split()))
onePos=P.index(1)
if onePos==0 :
    if P[1]==2:
        print(0)
    else:
        print(2)
elif onePos==N-1:
    if P[onePos-1]==2:
        print(1)
    else:
        print(3)
elif P[onePos-1]==2: #逆順
    if onePos+1 < N-onePos:
        t=onePos+2 #裏返し元に戻す
    else:
        t=N-onePos 
    print(t) 
else: #正
    if onePos < N-onePos+2:
        t=onePos
    else:
        t=N-onePos+2 #裏返してもと戻す
    print(t)

    
