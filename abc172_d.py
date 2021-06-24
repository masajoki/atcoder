N=int(input())
divs=[0 for _ in range(N+1)]
for n in range(1,N+1):
    for m in range(n,N+1,n):
        divs[m]+=1

ans=0
for i in range(N+1):
    ans+=i*divs[i]
print(ans)

# 回答の通り実装した。
# 回答見ても意味がわからなかったけど、実装みたら簡単だった。。。。
# 約数は素因数分解するより、実際に掛け算して倍数をつくってったほうが簡単なようだ。
# でもpypy3で速度がギリギリ。間に合わなそうだという感覚は正しかった。python3, cythonでは通らない。