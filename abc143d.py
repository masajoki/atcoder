# わからんかったの回答を見た
# Lをsort
# 2つ(a,b)選ぶ。これは大きいものとして、cはこれより小さいのから選ぶ。
# 小さいの(c)は >|a-b|であれば三角形を作れる。
#ざっくり10^3^2の組み合わせがあって、10^3こを10^3回サーチするとトータルで 10^9担ってしまって間に合わないので、
# c>abs(a-b)をバイナリサーチすればまにあう
# bisectは便利・・・ 
import bisect
N=int(input())
L=list(map(int,input().split()))
L.sort()

ans=0
for i in range(1,N-1):
    for j in range(i+1,N):
        a=L[i]
        b=L[j]
        tofind=abs(a-b)+1
        # bisectはソートされているリストのどこに入れることができるかを探す
        index=bisect.bisect_left(L,tofind,0,i)
        ans+=(i-index)

print(ans)