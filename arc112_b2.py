B,C=map(int,input().split())
if B==0:
    ans=(C-1)//2-(-C//2)+1
    print(ans)
elif B<0:
    if B< (-B-(C-1)//2 ):
        t1=B-(B-C//2)+1
        t2=-B+(C-1)//2-(-B-(C-1)//2)+1
        print(t1+t2)
    else:
        t1=-B+(C-1)//2-(B-C//2)+1
        print(t1)
else:
    if -B+(C-1)//2 <= B-(C-1)//2:
        t1=-B+(C-1)//2-(-B-(C-1)//2)+1
        t2=B-(B-(C//2))+1
        print(t1+t2)
    elif B>= -B+(C-1)//2 > B-(C/2):
        t1=B-(-B-(C-1)//2)+1
        print(t1)
    else:
        t1=-B+(C-1)//2-(-B-(C-1)//2)+1
        print(t1)
    