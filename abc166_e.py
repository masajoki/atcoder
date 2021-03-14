N=int(input())
A=list(map(int,input().split()))
Dif=[0 for _ in range(N+1)]
for i in range(N):
    d=(i+1)-A[i]
    if d>0 and d<=N:
        Dif[d]+=1
ans=0
for i in range(N):
    if 0<i+1+A[i]<=N:
        ans+=Dif[i+1+A[i]]
print(ans)
# １時間以上かかったが自力でできた。
# j-i= A[i]+A[j]
# j-A[j]= A[i]+i
# なので
# j-A[j] の値をインデックスにした配列に個数を入れておいて、
# A[i]+i をインデックスにして配列から個数を取り出せば良い
# j-A[j] はNを超えることがないのでそれぐらいのサイズの配列でOK。