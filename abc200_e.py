N,K=map(int,input().split())
temp=0
last=0
ijk=0
for n in range(3,3*N+1):
    temp=(n-1)*(n-2)//2 #i+j+k=nのときの、i,j,kの組み合わせ数
    if last+temp >= K: #n=3 ... の組み合わせの数を足し合わせたときに、Kを越える組み合わせの数
        ijk=n
        break
    else:
        last+=temp
# i,k,jの合計がijkのとき、 ijkをi,k,jの組み合わせに分割して, i,j の順に並び替えたときに、K-last番目になる i,j, (ijk-i,j) が答えかな

# print(ijk)
# print(K-last)

T=K-last
found=0
for i in range(1,ijk-2+1):
    if T-(ijk-i-1)<=0:
        found=i-1
        break   
    T-=(ijk-i-1)

print(i,T-i+1,(ijk-(T-i+1)))

