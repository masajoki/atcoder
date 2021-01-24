N=int(input())
A=list(map(int,input().split()))
start=0


# 山の雨をm1, m2, m3とし、ダムの水量をd1,d2,d3..とすると、
# d1=(m1+m2)/2, d2=(m2+m3)/2, ... dn=(mn+m1)/2 なので
# d1-d2+d3-d4..+dn = 2*m1/2 となるので、
# それをいい感じに計算した。もっと簡単だったみたい。

Pstart=[]
Mstart=[]

psum=0
msum=0
for i in range(N):
    if i%2==0:
        psum+=A[i]
        msum+=-1*A[i]
    else:
        psum+=-1*A[i]
        msum+=A[i]
    Pstart.append(psum)
    Mstart.append(msum)

for i in range(N):
    if i%2==0:
        if i-1>=0:
            print(Mstart[i-1]-Pstart[i-1]+Pstart[N-1], end=" ")
        else:
            print(Pstart[N-1], end=" ")
    else:
        if i-1>=0:
            print(Pstart[i-1]-Mstart[i-1]+Mstart[N-1], end=" ")
        else:
            print(Mstart[N-1], end=" ")
print()
