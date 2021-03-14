X,Y,A,B,C=map(int,input().split())
P=list(map(int,input().split()))
Q=list(map(int,input().split()))
R=list(map(int,input().split()))
P.sort()
P.reverse()
Q.sort()
Q.reverse()
R.sort()
Px=P[:X]
Qy=Q[:Y]
T=[]
for i in range(C-1,-1,-1):
    if len(Px) >0 and len(Qy)>0:
        if R[i]>Px[-1] or R[i]>Qy[-1]:
            if Px[-1]>=Qy[-1]:
                Qy.pop()
                T.append(R[i])
            else:
                Px.pop()
                T.append(R[i])
    elif len(Px) >0 and len(Qy)==0:
        if R[i]>Px[-1]:
            Px.pop()
            T.append(R[i])
    elif len(Px) ==0 and len(Qy)>0:
        if R[i]>Qy[-1]:
            Qy.pop()
            T.append(R[i])
    else:
        break

print(sum(Px)+sum(Qy)+sum(T))
