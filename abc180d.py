X,Y,A,B=map(int,input().split())

k=0 #経験値
kakoG=0
atG=0
while (A-1)*X<B and X*A < Y:
    X*=A
    kakoG+=1

if (Y-X)%B==0:
    atG=(Y-X)//B-1
else:
    atG=(Y-X)//B
print(X,Y,A,B)
print(kakoG+atG)