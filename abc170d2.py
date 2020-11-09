## 回答動画を見てそのまま実装した。

from sys import stdin

def main():
    n=int(input())
    As=list(map(int, stdin.readline().split()))
    As.sort()

    # エラトステネスの篩みたいなやりかた。倍数にフラグを立てていく。
    # 各要素の倍数の数字に1をインクリメントしていく。1以上なら、他の数字で割り切れるということ（頭良すぎ）
    check=[0]*(10**6+10)
    for a in As:
        count=1
        while a*count < 10**6+2 and a*count < As[-1]+1:
            # 2を超えていたらそれ以上増やす必要がない
            if check[a*count]<2:
                check[a*count]+=1
            count+=1
    ans=0
    for a in As:
        if check[a]==1:
            ans+=1
    print(ans)


if __name__ == '__main__':
    main()