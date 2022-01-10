#abc190_d
# D - Staircase Sequences 
# https://atcoder.jp/contests/abc190/tasks/abc190_d
# 整数からなる公差 1 の等差数列のうち、総和が N であるものはいくつあるでしょうか？
# 1<=N<=10**12
# 等差数列の和の公式は N*(2*I + N-1)//2
N=int(input())
ans=0
for i in range(1,10**7): #等差数列の和の公式をNを固定してIが整数になるなら選択肢になる。
    #初項がマイナスになるパターンは初項がプラスになるパターンの裏返しなのでプラスになる場合だけ考えれば良い
    t=(2*N+i-i**2)
    if t<=0:
        break

    #あまりがゼロなら初項が整数になる
    r=(2*N+i-i**2)%(2*i)
    if r==0:
        I=(2*N+i-i**2)//(2*i) 

        # print("I="+str(I)+" n="+str(i))
        ans+=2
print(ans)

#なんか公式回答とぜんぜん違うみたいだけどACにはなる