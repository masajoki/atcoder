#最終形の境界を動かしていくやりかた

N=int(input())
C=input()

ans=N
countR=0 #境界の右側にあるR
countW=0 #境界の左側にあるW
for c in C:
    if c=='R':
        countR+=1

ans=max(countR, countW)  #境界が左端のとき

for c in C: #i は境界,i=0のとき境界は左端をすべてRに、右をすべてWにする
    if c=='W':
        countW+=1
    else:
        countR-=1
    temp=max(countR, countW)
    ans=min(ans,temp)
print(ans)

